from django.urls import path, include
from . import views

urlpatterns = [
  path('profile/<str:pk>', views.userprofile, name='userprofile'),
  path('login/', views.user_login, name='login'),
  path('signup/', views.user_signup, name='signup'),
  path('logout/', views.user_logout, name='logout'),
  ]