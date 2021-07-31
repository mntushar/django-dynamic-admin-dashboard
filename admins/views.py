from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.core.paginator import Paginator
from user_login.forms import UserPassForm
from admins.models import EmployInfo
from .decorator import*
from .models import*
from .forms import*


#user role create start
@login_required
@write_required
def userrole(request):
    role_forms = UserRoleForm()
    if request.method == 'POST':
        role_forms = UserRoleForm(request.POST)
        if role_forms.is_valid():
            role_obj = role_forms.save(commit=False)
            role_obj.superuser = False
            role_obj.save()
            return redirect('user-role-list')

            
    context={
        'role_forms':role_forms,
    }
    return render(request, 'admins/user_role/role_form.html', context)

#user role create end


#user role list start
@login_required
@read_required
def rolelist(request):
    user_role = UserRole.objects.all()
    paginator = Paginator(user_role, 25)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context ={
        'contacts':contacts,
        'paginator':paginator,
    }
    return render(request, 'admins/user_role/role_list.html', context)
#user role list end


#edit user role start
@login_required
@edit_required
def userroleedit(request, pk):
    user_role = UserRole.objects.get(id=pk)
    user_role_form = UserRoleForm(instance=user_role)
    if request.method == 'POST':
        role_forms = UserRoleForm(request.POST, instance=user_role)
        if role_forms.is_valid():
            role_forms.save()
            return redirect('user-role-list')

            
    context={
        'role_forms':user_role_form,
    }
    return render(request, 'admins/user_role/edit_user_role.html', context)

#edit user role end


#add employ start
@login_required
@write_required
def employadd(request):
    user_role = DesignationForm()
    employ_basic_forms = EmployBasicInfoForm()
    employ_academic_forms = EmployAcademicFormSet(queryset=EmployAcademicInfo.objects.none())
    employ_address_forms = EmployAddressInfoForm()
    employ_password_forms = UserPassForm()
    if request.method == 'POST':
        employ_basic_forms = EmployBasicInfoForm(request.POST)
        user_role_id = request.POST['designation_selection']
        employ_academic_forms = EmployAcademicFormSet(request.POST)
        employ_address_forms = EmployAddressInfoForm(request.POST)
        employ_password_forms = UserPassForm(request.POST)
        if employ_basic_forms.is_valid() and employ_academic_forms.is_valid() and employ_address_forms.is_valid() and employ_password_forms.is_valid():
            p = employ_password_forms.cleaned_data['password']
            rp = employ_password_forms.cleaned_data['repassword']
            name = employ_basic_forms.cleaned_data['name']
            email = employ_basic_forms.cleaned_data['email']
            if p==rp:
                employ_pass_obj = User.objects.create_user(username=email, password=p, email=email, first_name=name, is_staff=True)
                employ_basic_forms_obj = employ_basic_forms.save(commit=False)
                employ_address_forms_obj = employ_address_forms.save(commit=False)


                employ_basic_forms_obj.employ_id = employ_pass_obj
                employ_basic_forms.save()


                instances = employ_academic_forms.save(commit=False)
                for instance in instances:
                    instance.employ_id = employ_pass_obj
                    instance.save()


                employ_address_forms_obj.employ_id = employ_pass_obj
                employ_address_forms.save()


                role = UserRole.objects.get(id=user_role_id)
                employ_info=EmployInfo.objects.create(
                        designation=role,
                        password=employ_pass_obj,
                        user_basic=employ_basic_forms_obj,
                        user_academic=instance,
                        user_address=employ_address_forms_obj,
                    )
                employ_info.save()
                return redirect('employ-list')

            else:
                errors = 'The password you entered is not same'
                context = {
                    'employ_basic_forms' : employ_basic_forms,
                    'employ_academic_forms':employ_academic_forms,
                    'employ_address_forms':employ_address_forms,
                    'employ_password_forms':employ_password_forms,
                    'errors':errors,
                    'user_role':user_role,
                }
                return render(request, 'admins/employ/add_employ.html', context) 
    context = {
        'employ_basic_forms' : employ_basic_forms,
        'employAcademicFormSet':employ_academic_forms,
        'employ_address_forms':employ_address_forms,
        'employ_password_forms':employ_password_forms,
        'user_role':user_role,
    }
    return render(request, 'admins/employ/add_employ.html', context) 
#add employ end


#employ list start
@login_required
@read_required
def listemploy(request):
    employ_list = EmployInfo.objects.all()
    paginator = Paginator(employ_list, 25)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)


    #search form submit
    search_form = EmplloySearchForm()
    if request.method == 'POST':
        search_form = EmplloySearchForm(request.POST)
        if search_form.is_valid():
            item = search_form.cleaned_data['search']
            employ_list = EmployInfo.objects.filter(user_basic__name__icontains=item) or EmployInfo.objects.filter(designation__role__icontains=item) or  EmployInfo.objects.filter(user_basic__email__icontains=item)
            paginator = Paginator(employ_list, 25)
            page = request.GET.get('page')
            contacts = paginator.get_page(page)
            context={
                'paginator':paginator,
                'contacts':contacts,
                'search_form':search_form,
            }       
            return render(request, 'admins/employ/employ_list.html', context)
    context={
        'paginator':paginator,
        'contacts':contacts,
        'search_form':search_form,
    }
    return render(request, 'admins/employ/employ_list.html', context)

#employ list end


#employ information edit 
#employ edit menu
@login_required
@edit_required
def employedit(request, pk):
    profile = EmployInfo.objects.get(id=pk)
    academic_id = profile.password.id
    academic_info = EmployAcademicInfo.objects.filter(employ_id=academic_id)
    context = {
        'profile':profile,
        'academic_info':academic_info,
    }
    return render(request, 'admins/employ/edit_employ.html', context)


#employ basic information update
@login_required
@edit_required
def basic_update(request, pk):
    basic_info = EmployBasicInfo.objects.get(id=pk)
    basic_info_form = EmployBasicInfoForm(instance=basic_info)
    user_role_form = DesignationForm()
    if request.method == 'POST':
        basic_info_form = EmployBasicInfoForm(request.POST, instance=basic_info)
        user_role_id = request.POST['designation_selection']
        if basic_info_form.is_valid():
            name = basic_info_form.cleaned_data['name']
            basic_info_obj = basic_info_form.save()
            role = UserRole.objects.get(id=user_role_id)
            use_id = basic_info.employ_id
            use_id.first_name = name
            use_id.save()
            employ_info_obj = use_id.employinfo
            employ_info_obj.designation = role
            employ_info_obj.save()
            return redirect('employ-list')
    context = {
        'basic_info_form':basic_info_form,
        'user_role_form':user_role_form,
    }
    return render(request, 'admins/employ/basic_info_update.html', context)


#employ academic information update
@login_required
@edit_required
def academic_update(request, pk):
    academic_info = EmployAcademicInfo.objects.get(id=pk)
    acedmic_info_form = EmployAcademicForm(instance=academic_info)
    if request.method == 'POST':
        acedmic_info_form = EmployAcademicForm(request.POST, instance=academic_info)
        if acedmic_info_form.is_valid():
            acedmic_info_form.save()
            return redirect('employ-list')
    context = {
        'acedmic_info_form':acedmic_info_form,
    }
    return render(request, 'admins/employ/academic_update.html', context)


#employ academic information update
@login_required
@edit_required
def address_update(request, pk):
    address_info = EmployAddressInfo.objects.get(id=pk)
    address_info_form = EmployAddressInfoForm(instance=address_info)
    if request.method == 'POST':
        address_info_form = EmployAddressInfoForm(request.POST, instance=address_info)
        if address_info_form.is_valid():
            address_info_form.save()
            return redirect('employ-list')
    context = {
        'address_info_form':address_info_form,
    }
    return render(request, 'admins/employ/address_update.html', context)
#employ information edit end


#delete employ start
@login_required
@delete_required
def employ_delete(request, pk):
    employ_info = EmployInfo.objects.get(id=pk)
    user = User.objects.get(id=employ_info.password.id)
    user.is_active = False
    user.save()
    return redirect('employ-list')
#delete employ end


#user menu permission start
#user select menu permission
@login_required
@write_required
def menuuser(request):
    user_role = DesignationForm()
    sbtitle = SbTitle.objects.all().values()
    sbtitle_form = SbTitleFormSet(initial=sbtitle, prefix='Title')
    sbitleelement = SbTitleElement.objects.all().values()
    sbitleelement_form = SbTitleElementFormSet(initial=sbitleelement, prefix='Element')
    if request.method == 'POST':
        user_role_id = request.POST['designation_selection']
        sbtitle_form = SbTitleFormSet(request.POST, initial=sbtitle, prefix='Title')
        sbitleelement_form = SbTitleElementFormSet(request.POST, initial=sbitleelement, prefix='Element')
        if sbtitle_form.is_valid() and sbitleelement_form.is_valid():
            role = UserRole.objects.get(id=user_role_id)
            sb_title = sbtitle_form.cleaned_data
            for idx, item in enumerate(sb_title):
                if item['sb_permission'] == True:
                    title_id = sbtitle[idx]['id']
                    title = SbTitle.objects.get(id=title_id)
                    title.user_role.add(role)


            sb_element = sbitleelement_form.cleaned_data
            for idx, item in enumerate(sb_element):
                if item['el_permission'] == True:
                    element_id = sbitleelement[idx]['id']
                    element = SbTitleElement.objects.get(id=element_id)
                    element.user_role.add(role)
            return redirect('menu-list')
            
    context = {
        'user_role':user_role,
        'sbtitle_form':sbtitle_form,
        'sbitleelement_form':sbitleelement_form,
    }
    return render(request, 'admins/user_role/user_permission.html', context)


#user permission list
@login_required
@read_required
def permission_list(request):
    user_all_role = UserRole.objects.all()
    permission = []
    for i in user_all_role:
        permission.append(i.sbtitle_set.all())
    context = {
        'zip_user':zip(user_all_role, permission),
    }
    return render(request, 'admins/user_role/user_permission_list.html', context)


#user remove menu permission
@login_required
@delete_required
def remove_permission(request, pk):
    user_role = UserRole.objects.get(id=pk)
    sbtitle = user_role.sbtitle_set.all().values()
    for i in sbtitle:
        i['sb_permission'] = True
    sbtitle_form = SbTitleRemoveFormSet(initial=sbtitle, prefix='Title')
    sbitleelement = user_role.sbtitleelement_set.all().values()
    for i in sbitleelement:
        i['el_permission'] = True
    sbitleelement_form = SbTitleRemoveElementFormSet(initial=sbitleelement, prefix='Element')
    if request.method == 'POST':
        sbtitle_form = SbTitleRemoveFormSet(request.POST, initial=sbtitle, prefix='Title')
        sbitleelement_form = SbTitleRemoveElementFormSet(request.POST, initial=sbitleelement, prefix='Element')
        if sbtitle_form.is_valid() and sbitleelement_form.is_valid():
            sb_title = sbtitle_form.cleaned_data
            for idx, item in enumerate(sb_title):
                if item['sb_permission'] == False:
                    title_id = sbtitle[idx]['id']
                    title = SbTitle.objects.get(id=title_id)
                    title.user_role.remove(user_role)


            sb_element = sbitleelement_form.cleaned_data
            for idx, item in enumerate(sb_element):
                if item['el_permission'] == False:
                    element_id = sbitleelement[idx]['id']
                    element = SbTitleElement.objects.get(id=element_id)
                    element.user_role.remove(user_role)
            return redirect('menu-list')
    context = {
        'sbtitle_form':sbtitle_form,
        'sbitleelement_form':sbitleelement_form,
    }
    return render(request, 'admins/user_role/remove_menu_permission.html',context)

#user menu permission end