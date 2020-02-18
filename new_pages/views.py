from django.shortcuts import render
from django.http import HttpResponse
from . models import sponsors as Spons
from .models import SponsorSerializer,robothonAbstract,roboExpoAbstract,RobothonSerializer,RoboExpoSerializer
from rest_framework import viewsets

def sponsors(request):
    all_sponsors = Spons.objects.all()
    return render(request,'new_page/sponsors.html',{'all_sponsors':all_sponsors})
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