from django.db import models
import uuid
from user.models import Profile


# Create your models here.


class Blog(models.Model):
    PUBLISH_STATUS_CHOICES = [
        ('published', 'Published'),
        ('pending_approval', 'Pending Approval'),
        ('pending_delete', 'Pending Delete')
    ]
    id = models.UUIDField(default=uuid.uuid4,
                          unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
    





