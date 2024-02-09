from django.contrib.auth import get_user_model
from ..models import Contrato, Otrosi
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
# import settings
from django.conf import settings

class ContratoSerializer(serializers.ModelSerializer):
    """serializer for docDriver model"""

    class Meta:
        model = Contrato
        fields = '__all__'

class OtrosiSerializer(serializers.ModelSerializer):
    """serializer for docDriver model"""

    class Meta:
        model = Otrosi
        fields = '__all__'