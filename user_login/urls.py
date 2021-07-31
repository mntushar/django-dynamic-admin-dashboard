from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.user_loging, name='home-deshboard'), #url for home deshboard
    path('userdata/', views.session_user, name='user-session'), #user session data url
    path('logout/', views.user_logout, name='user-logout'), #user logout url
    path('profile/', views.profileuser, name='user-profile'), #user profile url
    path('changepass/', views.passchange, name='user-pass-change'), #user password change url
    path('userprofileedit/', views.editprofile, name='user-profile-edit'), #user profile edit url

]