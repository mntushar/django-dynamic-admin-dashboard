from django.urls import path
from .import views

urlpatterns = [
    path('', views.user_home, name='home-deshboard'), #user home url
    path('mainurl', views.rehome, name='main-url'), #redirect main url

]