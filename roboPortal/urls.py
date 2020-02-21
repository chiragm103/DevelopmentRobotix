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
app_name = 'portal'
urlpatterns = [
    path('',views.home,name= "home"),
    path('api/',views.home_api,name= "home_api"),
    path('createProfile/', views.createProfile, name="createProfile"),
    path('adminView/',views.adminView, name= "adminView"),
    path('profileView/<int:user_id>/',views.profileView, name= "profileView"),
    path('select/<int:team_id>',views.select, name="select"),
    path('confirm/<str:token>/',views.confirm, name="confirm"),
]
