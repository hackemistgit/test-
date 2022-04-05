from django.contrib import admin
from .models import DonorList
from django_otp.admin import OTPAdminSite


class DonorListShow(admin.ModelAdmin):
    list_display = ['name', 'Priority', 'home_address','aadhar_num','blood_group']

admin.site.register(DonorList, DonorListShow)
