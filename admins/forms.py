from django import forms
from django.forms import ModelForm
from django.forms import formset_factory, modelformset_factory
from .models import*


#user role form start
class UserRoleForm(ModelForm):
    class Meta:
        model = UserRole
        exclude = ['superuser']
        widgets = {
            'role' : forms.TextInput(attrs={'class':'form-control form-control-lg form-control form-control-lg-lg', 'placeholder':'Enter user role name', 'required':'True'}),
            'permission_read' : forms.CheckboxInput(),
            'permission_edit' : forms.CheckboxInput(),
            'permission_write' : forms.CheckboxInput(),
            'permission_delete' : forms.CheckboxInput(),
            
        }
#user role form end


#employ designation form start
class DesignationForm(forms.Form):
    designation_selection = forms.ModelChoiceField(queryset=UserRole.objects.exclude(superuser=True), empty_label="--------", widget=forms.Select(attrs={'class': 'form-control form-control-lg', 'placeholder':"Enter Password", 'required':'True'}))
#employ designation form end


#employ information form start
#employ basic information form
class EmployBasicInfoForm(ModelForm):
    class Meta:
        model = EmployBasicInfo
        exclude = ['employ_id']
        labels = {
            'name': 'Enter Employ Name',
            'gender': 'Select Employ Gender',
            'date_of_birth': 'Select Employ Date Of Birth',
            'phone_number': 'Enter Employ Phone Number',
            'email':'Enter Employ Email'

        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your name', 'required':'True'}),
            'gender' : forms.Select(attrs={'class':'form-control form-control-lg', 'required':'True'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control form-control-lg', 'type':'date', 'required':'True'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter phone number',  'required':'True'}),
            'email' : forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter phone number',  'required':'True'}),
        }


#employ academic information model form
class EmployAcademicForm(ModelForm):
    class Meta:
        model = EmployAcademicInfo
        exclude = ['employ_id']
        labels = {
            'degree': 'Enter Employ Degree',
            'last_passing_institution_name': 'Enter Employ Passing Institution',
            'last_passing_year': 'Enter Employ Passing Year',
            
        }
        widgets = {
            'degree' : forms.Select(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter degree'}),
            'last_passing_institution_name' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter institution name'}),
            'last_passing_year' : forms.DateInput(attrs={'class':'form-control form-control-lg', 'type':'date'}),
            
        }



#employ academic information modelformset formset
EmployAcademicFormSet = modelformset_factory(
    EmployAcademicInfo,
    exclude = ['employ_id'],
    extra=1,
    labels = {
        'degree': 'Enter Employ Degree',
        'last_passing_institution_name': 'Enter Employ Passing Institution',
        'last_passing_year': 'Enter Employ Passing Year',
        
    },
    widgets = {
        'degree' : forms.Select(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter degree'}),
        'last_passing_institution_name' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter institution name'}),
        'last_passing_year' : forms.DateInput(attrs={'class':'form-control form-control-lg', 'type':'date'}),
        
    },
    )


#employ address information form
class EmployAddressInfoForm(ModelForm):
    class Meta:
        model = EmployAddressInfo
        exclude = ['employ_id']
        labels = {
            'house_no': 'Enter Employ House Number',
            'thana_name': 'Enter Employ Thana Name',
            'district_name': 'Enter Employ District Name',
            'village_name': 'Enter Employ Village Name',
            'post_office': 'Enter Employ Post Office Name',
            
        }
        widgets = {
            'house_no' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter House Number', 'required':'True'}),
            'village_name' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter village name', 'required':'True'}),
            'post_office' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter post office', 'required':'True'}),
            'thana_name' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter thana', 'required':'True'}),
            'district_name' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter district', 'required':'True'}),
            
        }
#employ information form end


#menu permission form start
#add user menu permission form start
#sidebar title tabale form
class SbTitleForm(forms.Form):
    sb_title = forms.CharField(required=False)
    sb_permission = forms.BooleanField(required=False)


#sidebar title tabale formset
SbTitleFormSet = formset_factory(SbTitleForm, extra=0)


#sidebar title elementtabale form
class SbTitlElementForm(forms.Form):
    el_title = forms.CharField(required=False)
    el_permission = forms.BooleanField(required=False)

    
#sidebar title element tabale formset
SbTitleElementFormSet = formset_factory(SbTitlElementForm, extra=0)
#add user menu permission form end


#remove user menu permission form start
#sidebar title tabale form
class SbTitleRemoveForm(forms.Form):
    sb_title = forms.CharField(required=False)
    sb_permission = forms.BooleanField(required=False)


#sidebar title tabale formset
SbTitleRemoveFormSet = formset_factory(SbTitleForm, extra=0)


#sidebar title elementtabale form
class SbTitlRemoveElementForm(forms.Form):
    el_title = forms.CharField(required=False)
    el_permission = forms.BooleanField(required=False)

    
#sidebar title element tabale formset
SbTitleRemoveElementFormSet = formset_factory(SbTitlElementForm, extra=0)
#remove user menu permission form end
#menu permission form end


#employ search form
class EmplloySearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Type to filter..."}))