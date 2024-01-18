from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('blog/<str:pk>/', views.singleBlog, name='singleBlog'),
  path('login/', views.user_login, name='login'),
  path('signup/', views.user_signup, name='signup'),
  path('logout/', views.user_logout, name='logout'),
  path('create/', views.create_blog_post, name='create_blog_post'),
  ]