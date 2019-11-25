from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UserProfileViewSet,accountView,loginView,registerView

router = DefaultRouter()
router.register('profiles',UserProfileViewSet,base_name='user-profile-viewset')

urlpatterns = [
    path('',include(router.urls)),
    path('user/',accountView,name='account_email_verification_sent'),
    path('login/',loginView,name='account_login'),
    path('register/',registerView,name='account_signup'),

]
