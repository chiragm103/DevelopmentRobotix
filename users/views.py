from django.shortcuts import render, redirect
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import UserProfile
from django.contrib.auth.models import auth
from .serializers import UserProfileSerializer
from .serializers import UserDetailsSerializer as UD
from rest_auth import views
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
import requests as rq
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
    if 'login' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email= email, password = password)
        if user != None:
            auth.login(request,user)
            return redirect('/robothon/')
        else:
            return render(request,'users/login.html',{'msg':"Invalid credentials"})
        """
        payload = {'email':email,'password':password}
        response = rq.post('http://127.0.0.1:8000/rest-auth/login/', json= payload)
        if response.status_code == 200 or response.status_code == 201:
            return redirect('/robothon/')
        elif response.status_code == 400 or response.status_code == 404:
            msg = "Invalid Credential"
            return render(request,'users/login.html',{'msg':msg})
        """
    return render(request,'users/login.html')

def registerView(request):
    if 'register' in request.POST:
        email = request.POST['email']
        name = request.POST['name']
        phone_no = request.POST['phone_no']
        password = request.POST['password']
        password1 = request.POST['password1']
        payload = {'email':email,'name':name,'phone_no':phone_no,'password':password,'password1':password1}
        response = rq.post('http://127.0.0.1:8000/rest-auth/registration/', json= payload)
        #data = my_response.json()
        if response.status_code in range(200,300):
            messages.success(request, 'A verification email has been sent. Please verify and login')
            return redirect('/profiles/login/')
        elif response.status_code in range(400,500):
            msg = "Invalid Credential"
            return render(request,'users/register.html',{'msg':msg})
    return render(request,'users/register.html')
def email_exists(request,email):
    if UserProfile.objects.filter(email = email).exists() :
        return HttpResponse("true")
    else:
        return HttpResponse("false")
def forgot_password(request):
    if 'forgot' in request.POST:
        email = request.POST['email']
        payload = {'email':email}
        response =rq.post('http://127.0.0.1:8000/rest-auth/password/reset/', json= payload)
        if response.status_code in range(200,300):
            return HttpResponse("Confirmation Email sent to you")
        else:
            return render(request,'users/forgot.html',{'msg':"Invalid Credentials"})
    return render(request,'users/forgot.html',{'msg':"Invalid Credentials"})
def forgot_change(request, uid, token):
    if request.method == "POST":
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        payload = {'new_password1':new_password1,'new_password2':new_password2,'uid':uid,'token':token}
        response =rq.post('http://127.0.0.1:8000/rest-auth/password/reset/confirm/',json= payload)
        if response.status_code in range(200,300):
            return HttpResponse("Password for the given email id changed")
        else:
            return render(request,'users/forgot_change.html',{'uid':uid,'token':token,'msg':"Invalid credentials"})
    return render(request,'users/forgot_change.html',{'uid':uid,'token':token})
@login_required
def change(request):

    if request.method == "POST":
        cur_password = request.POST['cur_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = auth.authenticate(email = request.user.email,password = cur_password)
        if user != None:
            if password1 == password2:
                user.set_password(password1)
                user.save()
                return HttpResponse("Password Sucessively changed")
            else:
                return render(request,'users/change.html',{'message':"Passwords do not match"})
        else:
            return render(request,'users/change.html',{'message':"Invalid password"})
        
    return render(request,'users/change.html')


