from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm
from .models import*


#student information form start
#student basic information form
class UserBasicInfoForm(ModelForm):
    class Meta:
        model = UserBasicInfo
        exclude = ['user_id']
        labels = {
            'name': 'Enter Your Name',
            'gender': 'Select Your Gender',
            'date_of_birth': 'Select Your Date of Birth',
            'phone_number': 'Enter Your Phone Number',
            'email':'Enter Your Email',
            'designation': 'Select Your Designation',
            
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your name', 'required':'True'}),
            'gender' : forms.Select(attrs={'class':'form-control form-control-lg', 'required':'True'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control form-control-lg', 'type':'date', 'required':'True'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter phone number',  'required':'True'}),
            'email' : forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter phone number',  'required':'True'}),
            'designation' : forms.Select(attrs={'class':'form-control form-control-lg', 'required':'True'}),
            
        }

#student academic information form
class UserAcademicInfoForm(ModelForm):
    class Meta:
        model = UserAcademicInfo
        exclude = ['user_id']
        labels = {
            'degree': 'Enter Your Last Passing Degree',
            'last_passing_institution_name': 'Enter Last Passing Institution Name',
            'last_passing_year': 'Enter Last Passing Year',
            
        }
        widgets = {
            'degree' : forms.Select(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your degree', 'required':'True'}),
            'last_passing_institution_name' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter institution name', 'required':'True'}),
            'last_passing_year' : forms.DateInput(attrs={'class':'form-control form-control-lg', 'type':'date', 'required':'True'}),
            
        }


#student address information form
class UserAddressInfoForm(ModelForm):
    class Meta:
        model = UserAddressInfo
        exclude = ['user_id']
        labels = {
            'house_no': 'Enter Your House Number',
            'village_name': 'Enter Your Village Name',
            'thana_name': 'Enter Your Thana Name',
            'post_office': 'Enter Your Post Office Name',
            'district_name': 'Enter Your District Name',
            
        }
        widgets = {
            'house_no' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter House Number', 'required':'True'}),
            'village_name' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter village name', 'required':'True'}),
            'post_office' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter post office', 'required':'True'}),
            'thana_name' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter thana', 'required':'True'}),
            'district_name' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter district', 'required':'True'}),
            
        }


#student information form end
