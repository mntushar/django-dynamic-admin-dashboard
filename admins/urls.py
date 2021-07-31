from django.urls import path, include
from .import views

urlpatterns = [
    path('role/', views.userrole, name='role-site'), #user role urls
    path('addemploy/', views.employadd, name='add-employ'), #add employ url
    path('kjdfd387hhgf8483<pk>45dkjhfurhuycx847hgdsfghg/editemp/', views.employedit, name='edit-employ'), #employ edit url
    path('basic/adasds7675hhgf4234324<pk>4543dbnvbn6546fgfgd/', views.basic_update, name='basic-edit-employ'), #employ basic edit url
    path('academic/afdfd7668jiuhiuh6476<pk>897jkhvcxh86786/', views.academic_update, name='acedmic-edit-employ'), #employ academic edit url
    path('address/skjijfdks7786kjdfodij765<pk>765jfhkdjs34355/', views.address_update, name='address-edit-employ'), #employ address edit url
    path('empde/lklk8785kjfkjf88<pk>54kljj8342/', views.employ_delete, name='delete-employ'), #employ delete url
    path('listemp/', views.listemploy, name='employ-list'), #employ list url
    path('listrole/', views.rolelist, name='user-role-list'), #user role list url
    path('roleedit/hdifhdui6631hadgugu21<int:pk>56ddhhhjhj7632', views.userroleedit, name='user-role-edit'), #user role edit url
    path('permission/', views.menuuser, name='menu-permission'), #user menu permission url
    path('menulist/', views.permission_list, name='menu-list'), #user permission list url
    path('menuremove/kjks23434jkjd43<int:pk>67hfjksh34621', views.remove_permission, name='menu-remove'), #user menu permission remove url

]