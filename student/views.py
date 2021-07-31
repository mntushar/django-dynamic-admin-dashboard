from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user_login.models import*
from user_login.forms import UserPassForm
from .forms import*
from .models import*


#add student
def adduser(request):
    user_basic_forms = UserBasicInfoForm()
    user_academic_forms = UserAcademicInfoForm()
    user_address_forms = UserAddressInfoForm()
    user_password_forms = UserPassForm()
    if request.method == 'POST':
        user_basic_forms = UserBasicInfoForm(request.POST)
        user_academic_forms = UserAcademicInfoForm(request.POST)
        user_address_forms = UserAddressInfoForm(request.POST)
        user_password_forms = UserPassForm(request.POST)
        if user_basic_forms.is_valid() and user_academic_forms.is_valid() and user_address_forms.is_valid() and user_password_forms.is_valid():
            p = user_password_forms.cleaned_data['password']
            rp = user_password_forms.cleaned_data['repassword']
            email = user_basic_forms.cleaned_data['email']
            name = user_basic_forms.cleaned_data['name']
            if p==rp:
                user_pass_obj = User.objects.create_user(username=email, password=p, email=email, first_name=name, is_staff=False)
                user_basic_forms_obj = user_basic_forms.save(commit=False)
                user_academic_forms_obj = user_academic_forms.save(commit=False)
                user_address_forms_obj = user_address_forms.save(commit=False)


                user_basic_forms_obj.user_id = user_pass_obj
                user_basic_forms.save()

                user_academic_forms_obj.user_id = user_pass_obj
                user_academic_forms.save()


                user_address_forms_obj.user_id = user_pass_obj
                user_address_forms.save()


                user_info=UserInfo.objects.create(
                        password=user_pass_obj,
                        user_basic=user_basic_forms_obj,
                        user_academic=user_academic_forms_obj,
                        user_address=user_address_forms_obj
                    )
                user_info.save()


                context = {
                    'user_info':user_info,
                }
                return render(request, 'login/user_save_conformation.html', context)
            else:
                errors = 'The password you entered is not same'
                context = {
                    'user_basic_forms' : user_basic_forms,
                    'user_academic_forms':user_academic_forms,
                    'user_address_forms':user_address_forms,
                    'user_password_forms':user_password_forms,
                    'errors':errors,
                }
                return render(request, 'login/add_user_forms.html', context)

    context = {
        'user_basic_forms' : user_basic_forms,
        'user_academic_forms':user_academic_forms,
        'user_address_forms':user_address_forms,
        'user_password_forms':user_password_forms,
    }
    return render(request, 'login/add_user_forms.html', context)
#add student end


#student part start.....
#student home start
@login_required
def student_home(request):
    student = 'student'
    context ={
        'student':student,
                
    }
    return render(request, 'home/index.html', context) 
#student home end

#student part end....
