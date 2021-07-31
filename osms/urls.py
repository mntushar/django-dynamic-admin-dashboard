"""osms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user_login import urls, views
from student import urls
from admins import urls
from home import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('user_login.urls'), name='userlogin-site'),#user login urls
    path('', include('home.urls'), name='home-site'),#user home deshboard urls
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='login/password_reset_form.html'), name='password_reset'), #url for password reset
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'), # url for password reset done
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'), # url for password reset confirm
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'), name='password_reset_complete'), # url for password reset complete
    path('student/', include('student.urls'), name='student-site'), #student urls
    path('admins/', include('admins.urls'), name='admin-site'), #user admin urls

]
