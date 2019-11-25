from rest_framework import serializers
from .models import DIY,FYI


class DIYSerializer(serializers.ModelSerializer):

    class Meta:
        model = DIY
        fields = "__all__"


class FYISerializer(serializers.ModelSerializer):

    class Meta:
        model = FYI
        fields = "__all__"
