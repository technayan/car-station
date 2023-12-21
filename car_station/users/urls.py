from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('register/', views.RegistrationView.as_view(), name = 'register'),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),
    path('profile/', views.profileView, name = 'profile'),
    path('edit-profile/', views.edit_profile, name = 'edit-profile'),
    path('change-password/', views.change_password, name = 'change-password'),
]
