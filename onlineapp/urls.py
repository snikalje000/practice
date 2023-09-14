

"""onlineweb URL Configuration




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




from django.urls import path

from .import views
from  django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

app_name = 'onlineapp'




urlpatterns = [

    path('',views.home,name='index'),
    path('about_us',views.about,name='about_us'),
    path('the_future_of_education/',views.the_future_of_education,name='blogsingle'),
    path('building_a_growth_mindset/',views.building_a_growth_mindset,name='blogsingle1'),
    path('work_education_balance/',views.work_education_balance,name='blogsingle2'),
    path('blog/',views.blog,name='blog'),
    path('privacy/',views.privacy,name='privacy'),
    path('terms/',views.terms,name='terms'),
    path('enrollnow/',views.enrollnow,name='enrollnow'),
    path('contact/',views.contact,name='contact'),
    path('AI-ML/',views.courses,name='courses'),
    path('instructordetails/',views.instructordetails,name='instructordetails'),
    path('instructor/',views.instructor,name='instructor'),
    path('Data_Science',views.coursedataanalytics,name='coursedataanalytics'),
    path('Cyber_Security/',views.coursecybersecurity,name='coursecybersecurity'),
    path('Cloud/',views.coursecloudcomputing,name='coursecloudcomputing'),
    path('enroll_data/', views.eroll_data, name='enroll_data'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('maildata/', views.maildata, name='maildata'),
    path('events/', views.events, name='events'),
    path('AI-ML/enroll_data/', views.eroll_data, name='enroll_data'),
    path('Data_Science/enroll_data/', views.eroll_data, name='enroll_data'),
    path('Cloud/enroll_data/', views.eroll_data, name='enroll_data'),
    path('Cyber_Security/enroll_data/', views.eroll_data, name='enroll_data'),
    path('chatview/', views.chatview, name='chatview'),
    path('sid/', views.phonedata1, name='sid'),  # URL for saving phone data
    path('popdata/',views.popdata,name='popdata'),
    path('blogger',views.blogs,name='blogger'),

    path('robots/',views.robots,name='robots'),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
    
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)



