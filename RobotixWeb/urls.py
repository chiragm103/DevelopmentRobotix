"""RobotixWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from allauth.account.views import confirm_email
from new_pages.views import sponsors,api_sponsors,abstract_robothon,abstract_expo,api_fest_expo,api_fest_robothon, verify_user
# from rest_auth.views import LoginView
router = routers.DefaultRouter()
router.register(r'sponsors', api_sponsors)
router.register(r'robofest/roboexpo', api_fest_expo)
router.register(r'robofest/robothon', api_fest_robothon)

urlpatterns = [
    path('rest-auth/registration/account-confirm-email/<str:key>/',verify_user, name="verify_user"),#over ride the rest auth urls
    path('api/', include(router.urls)),
    path('devtainsaan/', admin.site.urls),
    path('',views.index,name='index'),
    path('aboutus/',include('about.urls')),
    path('events/',include('events.urls')),
    path('gallery/',include('gallery.urls')),
    path('achievements/',include('achievements.urls')),
    path('contactus/',include('contact.urls')),
    path('info/',include('extras.urls')),
    path('alumni/',include('alumni.urls')),
    path('webteam',views.webteam,name='webteam'),
    path('', include('django.contrib.auth.urls')), 
    # path('form',views.form,name='form'),
    path('profiles/',include('users.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/',include('rest_auth.urls')),
    path('robothon/',include('roboPortal.urls')),
    path('sponsors/',sponsors, name= "sponsors"),
    path('robofest/roboexpo/',abstract_expo, name="abstract_expo"),
    path('robofest/robothon/',abstract_robothon, name="abstract_robothon"),
    # path('accounts-rest/registration/account-confirm-email/<key>/', LoginView.as_view(), name='account_confirm_email'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
