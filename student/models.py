from django.db import models
from django.contrib.auth.models import User


#student information table start
#student address information table
class UserAddressInfo(models.Model):
    house_no = models.CharField(max_length = 50, blank=True, null=True)
    village_name = models.CharField(max_length = 50, blank=True, null=True)
    post_office = models.CharField(max_length = 50, blank=True, null=True)
    thana_name = models.CharField(max_length = 50, blank=True, null=True)
    district_name = models.CharField(max_length = 50, blank=True, null=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user_id.first_name


#student academic information table
class UserAcademicInfo(models.Model):
    degree_choices=[
        ('psc',"PSC"),
        ("jsc","JSC"),
        ('ssc',"SSC"),
        ("hsc","HSC"),
        ('bsc-engineering',"Bsc.Engineering"),
        ('m.engineering',"M.Engineering"),
        ('d.engr.',"D.Engr."),
        ("doctor","Doctor"),
        ("md","MD"),
        ("ph.d","Ph.D"),
        ('b.sc.',"B.sc."),
        ('m.sc.',"M.sc."),
        ("bba","BBA"),
        ("mba","MBA"),
        ('ba',"BA"),
        ('ma',"Ma"),
    ]
    degree = models.CharField(
        max_length=100, blank=True, null=True,
        choices=degree_choices,
        )
    last_passing_institution_name = models.CharField(max_length = 100, blank=True, null=True)
    last_passing_year = models.DateField(blank=True, null=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user_id.first_name


#student basic information table
class UserBasicInfo(models.Model):
    name = models.CharField(max_length = 100, blank=True, null=True)
    gender_choices=[
        ('male',"Male"),
        ("female","Female"),
    ]
    gender = models.CharField(
        max_length=6, blank=True, null=True,
        choices=gender_choices,
        )
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True, error_messages={'unique':"This email has already been registered."})
    designation_choices=[
        ('student',"Student"),
    ]
    designation = models.CharField(
        max_length=10, blank=True, null=True,
        choices=designation_choices,
    )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
        

    def __str__(self):
        return self.name


#student user information table
class UserInfo(models.Model):
    password = models.OneToOneField(User, on_delete=models.CASCADE)
    user_basic = models.OneToOneField(UserBasicInfo, blank=True, null=True, on_delete=models.CASCADE)
    user_academic = models.OneToOneField(UserAcademicInfo, blank=True, null=True, on_delete=models.CASCADE)
    user_address = models.OneToOneField(UserAddressInfo, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.uses_basic.name


#student information table end