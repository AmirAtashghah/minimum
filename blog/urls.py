from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('blog/<str:pk>/', views.single_blog, name='single_blog'),
  path('create/', views.create_blog_post, name='create_blog_post'),
  ]