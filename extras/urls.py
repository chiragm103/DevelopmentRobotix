from django.urls import path
from . import views
app_name = 'info'
urlpatterns = [
    path('diy/',views.diy,name='diy'),
    path('fyi/',views.fyi,name='fyi')
]
