from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from admins.models import*
from .forms import*
from .models import*


#user loging
def user_loging(request):
    loging_form = UserLogingForm()
    if request.method == 'POST':
        loging_form = UserLogingForm(request.POST)
        if loging_form.is_valid():    
            name = loging_form.cleaned_data['name']
            password = loging_form.cleaned_data['password']
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error_loging = 'The email and password that you entered did not match our records. Please double-check and try again.'
                context = {
                    'loging_form':loging_form,
                    'error_loging':error_loging,
                }
                return render(request, 'login/user_login.html', context)
    context = {
        'loging_form':loging_form
    }
    return render(request, 'login/user_login.html', context)


#user session sidebar data 
def session_user(request):
    user = request.user
    role = user.employinfo.designation
    section = SbSection.objects.all()
    title = role.sbtitle_set.all()
    element = role.sbtitleelement_set.all()
    session_section = {}
    session_title = {}
    session_element = {}
    #dictionary value for section
    for i in section:
        session_section[i.id] = {'title':i.section_title}
    #dictionary value for title
    for i in title:
        if i.section_title == None:
            session_title[i.id] = {'title':i.sb_title, 'icone':i.icone, 'section_id':0}
        else:
            session_title[i.id] = {'title':i.sb_title, 'icone':i.icone, 'section_id':i.section_title.id}
    #dictionary value for element
    for i in element:
        session_element[i.id] = {'title':i.el_title, 'url':i.url, 'title_id':i.sbtitle_id.id}
    dic_sidebar = {
        'section':session_section,
        'title':session_title,
        'element':session_element,
    }
    request.session['dynamic_sidebar'] = dic_sidebar
    return redirect('/')
    

#user logout
def user_logout(request):
    logout(request)
    return redirect('/')


#user profile
@login_required
def profileuser(request):
    recent_user = request.user
    if recent_user.is_staff == True:
        user_profile = recent_user.employinfo
    else:
        user_profile = recent_user.userinfo
    
    context = {
       'user_profile':user_profile, 
    }
    return render(request, 'login/user_profile.html', context)


#change password of user
@login_required
def passchange(request):
    user = request.user
    pass_forms = UserPassChangeForm()
    if request.method == 'POST':
        pass_forms = UserPassChangeForm(request.POST)
        if pass_forms.is_valid():
            newp = pass_forms.cleaned_data['password']
            newrp = pass_forms.cleaned_data['repassword']
            if newp == newrp:
                username = user.username
                user = User.objects.get(username=username)
                user.set_password(newp)
                user.save()
                return redirect('home-deshboard')
    context = {
        'pass_forms':pass_forms,
    }
    return render(request, 'login/change_pass.html', context)


#edit user profile
@login_required
def editprofile(request):
    user = request.user
    email = user.username
    userinfo = UserInfo.objects.get(email=email)
    edit_forms = UserInfoForm(instance=userinfo)
    if request.method == 'POST':
        edit_forms = UserInfoForm(request.POST, instance=userinfo)
        if edit_forms.is_valid():
            edit_forms.save()
            return redirect('user-profile')
    context ={
        'edit_forms':edit_forms,
    }
    return render(request, 'login/profile_edit.html', context)

