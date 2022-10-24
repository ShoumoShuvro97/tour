from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Signup, name="signuppage"),
    path('login/', views.Login, name="loginpage"),
    path('logout/', views.Logout, name="logoutpage"),
    path('profile/', views.Profile, name="profilepage"),
]
