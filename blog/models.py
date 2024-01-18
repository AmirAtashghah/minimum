from django.db import models
from django.contrib.auth.models import User
import uuid



# Create your models here.

class Profile(models.Model):
    USER_ROLES = [
        ('reader', 'Reader'),
        ('writer', 'Writer'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                 null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='reader')
    profile_picture = models.ImageField(upload_to='profileImages/', null=True,
                                         blank=True)
    id = models.UUIDField(default=uuid.uuid4,
                          unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.user.username



class Blog(models.Model):
  
    id = models.UUIDField(default=uuid.uuid4,
                          unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    edit_request = models.BooleanField(default=False)
    delete_request = models.BooleanField(default=False)
    tags = models.CharField(max_length=20,null=True)
    image = models.ImageField(upload_to='blogImages/', null=True, blank=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          unique=True, primary_key=True, editable=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True,
                                blank=True, default="guest")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.content
    





