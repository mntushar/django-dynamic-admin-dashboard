from django.db import models
from django.contrib.auth.models import User


#user role table
class UserRole(models.Model):
    role = models.CharField(max_length = 100, blank=True, null=True)
    permission_read = models.BooleanField(null=True)
    permission_edit = models.BooleanField(null=True)
    permission_write = models.BooleanField(null=True)
    permission_delete = models.BooleanField(null=True)
    superuser = models.BooleanField(null=True)


    def __str__(self):
        return self.role

#end user role table


#employ information table start
#employ address information table
class EmployAddressInfo(models.Model):
    house_no = models.CharField(max_length = 50, blank=True, null=True)
    village_name = models.CharField(max_length = 50, blank=True, null=True)
    post_office = models.CharField(max_length = 50, blank=True, null=True)
    thana_name = models.CharField(max_length = 50, blank=True, null=True)
    district_name = models.CharField(max_length = 50, blank=True, null=True)
    employ_id = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.employ_id.first_name


#employ academic information table
class EmployAcademicInfo(models.Model):
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
    employ_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.degree


#employ basic information table
class EmployBasicInfo(models.Model):
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
    employ_id = models.OneToOneField(User, on_delete=models.CASCADE)
        

    def __str__(self):
        return self.name


#employ employ information table
class EmployInfo(models.Model):
    password = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.ForeignKey(UserRole, blank=True, null=True, on_delete=models.CASCADE)
    user_basic = models.OneToOneField(EmployBasicInfo, blank=True, null=True, on_delete=models.CASCADE)
    user_academic = models.OneToOneField(EmployAcademicInfo, blank=True, null=True, on_delete=models.CASCADE)
    user_address = models.OneToOneField(EmployAddressInfo, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.user_basic.name


#employ information table end


#user menu permission table start
#sidbar menu section
class SbSection(models.Model):
    section_title = models.CharField(max_length = 100, blank=True, null=True)


    def __str__(self):
        return self.section_title


#sidebar title table
class SbTitle(models.Model):
    sb_title = models.CharField(max_length = 100, blank=True, null=True)
    icone = models.CharField(max_length=100, blank=True, null=True)
    section_title = models.ForeignKey(SbSection, blank=True, null=True, on_delete=models.PROTECT)
    user_role = models.ManyToManyField(UserRole, blank=True)


    def __str__(self):
        return self.sb_title


#sidebar title element table
class SbTitleElement(models.Model):
    el_title = models.CharField(max_length = 100, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    sbtitle_id = models.ForeignKey(SbTitle, blank=True, null=True, on_delete=models.PROTECT)
    user_role = models.ManyToManyField(UserRole, blank=True)


    def __str__(self):
        return self.el_title

#user menu permission table end