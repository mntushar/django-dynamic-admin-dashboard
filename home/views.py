from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from student.models import UserInfo
from admins.models import*


# home view
@login_required
def user_home(request):
    user = request.user
    #check dynamic sidebar value
    if user.is_staff == True:
        role = user.employinfo.designation
        element = role.sbtitleelement_set.all()
        sidebar = request.session.get('dynamic_sidebar')
        if sidebar is None or not bool(sidebar):
            return redirect('user-session')
        else:
            session_element = sidebar['element']
            if len(session_element) != len(element):
                request.session.get('dynamic_sidebar').clear()
                return redirect('/')
            else:
                for ind, item in enumerate(session_element):
                    if str(item) != str(element[ind].id):
                        request.session.get('dynamic_sidebar').clear()
                        break
                        return redirect('/')
                return render(request, 'home/index.html')
    else:
        return render(request, 'home/index.html')
    
    

#redirect main url
@login_required
def rehome(request):
    return redirect('/')


