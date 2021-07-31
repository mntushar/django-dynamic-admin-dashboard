from django.urls import path, include
from .import views

urlpatterns = [
    path('adduser/', views.adduser, name='adduser'), #add student url
    path('home/', views.student_home, name='student-home'), #student home url    
    

]