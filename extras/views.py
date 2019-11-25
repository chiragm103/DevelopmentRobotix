from django.shortcuts import render
from .models import FYI,DIY
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DIYSerializer,FYISerializer
# Create your views here

@api_view()
def diy(request):
    obj_diy = DIY.objects.all()
    serializer = DIYSerializer(obj_diy,many=True)
    dict = {'diy':serializer.data}
    # return render(request,'diy.html',context=dict)
    return Response(dict)

@api_view()
def fyi(request):
    obj_fyi = FYI.objects.all()
    serializer = FYISerializer(obj_fyi,many=True)
    dict = {'fyi':serializer.data}
    # return render(request,'fyi.html',context=dict)
    return Response(dict)
