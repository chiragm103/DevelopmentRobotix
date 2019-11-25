from django.urls import path
from . import views
urlpatterns = [
    path('',views.alumni,name='alumni')
]
