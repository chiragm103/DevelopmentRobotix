from django.shortcuts import render, redirect
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from .serializers import UserDetailsSerializer as UD
from rest_auth import views
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
import requests as rq
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = ''


class UserDetailsView(RetrieveUpdateAPIView):
    """
    Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.

    Default accepted fields: username, first_name, last_name
    Default display fields: pk, username, email, first_name, last_name
    Read-only fields: pk, email

    Returns UserModel fields.
    """
    serializer_class = UD
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        """
        Adding this method since it is sometimes called when using
        django-rest-swagger
        https://github.com/Tivix/django-rest-auth/issues/275
        """
        return get_user_model().objects.none()

def accountView(request):
    return render(request,'confirm.html')

def loginView(request,message = None):
    return render(request,'users/login.html')

def registerView(request):
    pass
    message = None
    if 'register' in request.POST:
        email = request.POST['email']
        name = request.POST['name']
        phone_no = request.POST['phone_no']
        password = request.POST['password']
        password1 = request.POST['password1']
        payload = {'email':email,'name':name,'phone_no':phone_no,'password':password,'password1':password1}
        my_response = rq.post('http://127.0.0.1:8000/rest-auth/registration/', json= payload)
        data = my_response.json()
        if data['detail'] and data['detail'] == "Verification e-mail sent.":
            messages.success(request, 'A verification email has been sent. Please verify and login')
            return redirect('/profiles/login/')
    return render(request,'users/register.html')
def email_exists(request,email):
    if UserProfile.objects.filter(email = email).exists() :
        return HttpResponse("true")
    else:
        return HttpResponse("false")
