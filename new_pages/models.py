from django.db import models
from rest_framework import serializers
class sponsors(models.Model):
    name = models.CharField(max_length= 150, null= True, blank= True)
    sponsor_type = models.CharField(max_length= 150, null= True, blank= True) 
    website = models.CharField(max_length= 150, null= True, blank= True) 
    phone_number = models.IntegerField(null= True, blank= True)
    logo = models.FileField(null= True, blank= True,upload_to='sponsors/')
class robothonAbstract(models.Model):
    title = models.CharField(max_length= 150, null= True, blank= True)
    xfile = models.FileField(null= True, blank= True,upload_to='robothonAbstract/')
class roboExpoAbstract(models.Model):
    title = models.CharField(max_length= 150, null= True, blank= True)
    xfile = models.FileField(null= True, blank= True,upload_to='robothonExpoAbstract/')
class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sponsors
        fields = '__all__'
class RobothonSerializer(serializers.ModelSerializer):
    class Meta:
        model = robothonAbstract
        fields = '__all__'
class RoboExpoSerializer(serializers.ModelSerializer):
    class Meta:
        model = roboExpoAbstract
        fields = '__all__'