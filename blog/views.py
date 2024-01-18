from django.shortcuts import render, HttpResponse
from .models import Profile, Blog, Comment
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import CustomUserCreationForm, LoginForm,BlogPostForm
from django.contrib.auth.decorators import login_required
from .models import Blog

# Create your views here.



def index(request):
    posts = Blog.objects.all()

    unique_tags_ordered = []
    for post in posts:
        if post.tags not in unique_tags_ordered:
            unique_tags_ordered.append(post.tags)
    
    
    return render(request, 'index.html', {'posts': posts, 'tags':unique_tags_ordered })

def blogs(request):
  blogs = Blog.objects.all()
  context = { 'blogs': blogs }
  return render(request, 'blog/blogs.html', context)



def singleBlog(request, pk):
  blog = Blog.objects.get(id=pk)
  comments = blog.comments.all()
  context = { 'blog': blog , 'comments': comments}
  return render(request, 'blog/singleBlog.html', context)






# signup page
def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')




@login_required 
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the post with the current user as the author
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            print(blog_post)
            blog_post.save()
            return redirect('create_post.html')  # Redirect to the post detail page
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})


# def load_posts(request):
#     posts = BlogPost.objects.all()
