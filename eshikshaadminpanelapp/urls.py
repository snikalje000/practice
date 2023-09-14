"""
URL configuration for eshikshaadminpanel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .import views

app_name='eshikshaadminpanelapp'

urlpatterns = [
    path('',views.home,name="index"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('news_letters/',views.news_letters,name="news_letters"),
    path('brouchers/',views.brouchers,name="brouchers"),
    path('enquiries/',views.enquiries,name="enquiries"),
    path('login/',views.user_login,name="user_login"),
    path('logout/',views.user_logout,name="user_logout"),
    path('update_contact_status/',views.update_contact_status,name="update_contact_status"),
    path('update_newsletters_status/',views.update_newsletters_status,name="update_newsletters_status"),
    path('update_brouchers_status/',views.update_brouchers_status,name="update_brouchers_status"),
    path('update_enquiry_status/',views.update_enquiry_status,name="update_enquiry_status")
]
