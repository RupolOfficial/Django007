"""pythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
import home.views as home_view
import donor.views as donor_view
import find_donor.views as find_donor_view
import  blood_request.views as blood_request_view
import  contact.views as contact_view
import  about.views as about_view
import log_in.views as log_in_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.home_views),
    path('home/', home_view.home_views),
    path('donor/', donor_view.donor_views),
    path('find_donor/', find_donor_view.find_donor_views),
    path('blood_request/', blood_request_view.blood_request_views),
    path('contact/', contact_view.contact_views),
    path('about/', about_view.about_views),
    path('log_in/', log_in_view.log_in_view),

]
