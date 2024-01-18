from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import CustomUserCreationForm, LoginForm

# Create your views here.


def userprofile(request, pk):
  user = Profile.objects.get(id=pk)
  context = {'user': user}
  return render(request, 'user/userprofile.html', context)



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


