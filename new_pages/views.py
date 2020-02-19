from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import sponsors as Spons
from .models import SponsorSerializer,robothonAbstract,roboExpoAbstract,RobothonSerializer,RoboExpoSerializer
from rest_framework import viewsets
import requests as rq


def sponsors(request):
    all_sponsors = Spons.objects.all()
    return render(request,'new_page/sponsors.html',{'all_sponsors':all_sponsors})
def verify_user(request,key):
    print(key)
    payload = {'key':key}
    my_response =rq.post('http://127.0.0.1:8000/rest-auth/registration/verify-email/', json= payload)#change to robotix.nitrr.ac.in before pushing to server
    data = my_response.json()
    if data['detail'] == "ok":
        return HttpResponse("verified")
    else:
        raise Http404("Unable to verify")
def register(request):
    return render(request,'new_page/register.html')
class api_sponsors(viewsets.ModelViewSet):
    queryset = Spons.objects.all()
    serializer_class = SponsorSerializer
def abstract_robothon(request):
    all_abstract = robothonAbstract.objects.all()
    return render(request,'new_page/abstract.html',{'all_abstract':all_abstract})
def abstract_expo(request):
    all_abstract = roboExpoAbstract.objects.all()
    return render(request,'new_page/abstract.html',{'all_abstract':all_abstract})
class api_fest_expo(viewsets.ModelViewSet):
    queryset = roboExpoAbstract.objects.all()
    serializer_class = RoboExpoSerializer
class api_fest_robothon(viewsets.ModelViewSet):
    queryset = robothonAbstract.objects.all()
    serializer_class = RobothonSerializer