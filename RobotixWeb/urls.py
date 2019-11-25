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
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from allauth.account.views import confirm_email
from rest_auth.views import LoginView
urlpatterns = [
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
    # path('form',views.form,name='form'),
    path('profiles/',include('users.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/',include('rest_auth.urls')),
    path('accounts-rest/registration/account-confirm-email/<key>/', LoginView.as_view(), name='account_confirm_email'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
