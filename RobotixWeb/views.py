from django.shortcuts import render,redirect
import datetime
import time
def index(request):
    return render(request,'index.html')


def webteam(request):
    return render(request,'webteam.html')
