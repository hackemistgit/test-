"""bloodsbanks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
##temporary to show two factor
from django_otp.admin import OTPAdminSite

###django admin custom
class OTPAdmin(OTPAdminSite):
    pass

from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from dreg.models import DonorList
from dreg.admin import DonorListShow
admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice)
admin_site.register(DonorList,DonorListShow)





urlpatterns = [
    path('crazyfrog/', admin_site.urls),
    path('dcrazyfrog/', admin.site.urls),
     path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    
    

    path('', include('home.urls'), name='homesite'),
    path('donorreg/', include('dreg.urls'), name='dregsite'),
    path('search/', include('search.urls'), name='searchsite'),
    path('about/', include('dabout.urls'), name='aboutsite'),
    path('contact/', include('contact.urls'), name='contactsite'),
    path('user/',include('user.urls')),
    
    
   
   
    
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
