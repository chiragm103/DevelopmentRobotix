from rest_framework import serializers
from .models import Convenor,Coordinator,Manager

class ConvenorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenor
        fields = '__all__'

class CoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinator
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
