from django.contrib import admin
from .models import UserProfile,BlogPost, Comment

admin.site.register(UserProfile)
admin.site.register(BlogPost)
admin.site.register(Comment)

