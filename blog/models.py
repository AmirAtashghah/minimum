from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_ROLES = [
        ('reader', 'Reader'),
        ('writer', 'Writer'),
        ('admin', 'Admin'),
    ]

    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True,null=True)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='reader')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username

class BlogPost(models.Model):
    PUBLISH_STATUS_CHOICES = [
        ('published', 'Published'),
        ('pending_approval', 'Pending Approval'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts_written')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=PUBLISH_STATUS_CHOICES, default='pending_approval')
    tags = models.CharField(max_length=20,null=True)
    comments = models.ManyToManyField('Comment')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

