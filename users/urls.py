from rest_framework.routers import DefaultRouter
from django.urls import path,include,re_path
from . import views
from .views import UserProfileViewSet,accountView,loginView,registerView

router = DefaultRouter()
router.register('profiles',UserProfileViewSet,base_name='user-profile-viewset')

urlpatterns = [
    path('',include(router.urls)),
    path('user/',accountView,name='account_email_verification_sent'),
    path('login/',loginView,name='account_login'),
    path('register/',registerView,name='account_signup'),
    #re_path(r'email_exists/(?P<data>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})$',views.email_exists,name="email_exists"),
    path('email_exists/<str:email>/',views.email_exists, name="email_exists"),
    path('forgot_password/',views.forgot_password, name="forgot_password"),
    path('change/',views.change, name="change"),
]
