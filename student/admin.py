from django.contrib import admin
from .models import *


# user information registration
admin.site.register(UserInfo)
admin.site.register(UserBasicInfo)
admin.site.register(UserAcademicInfo)
admin.site.register(UserAddressInfo)
