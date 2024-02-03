from django.contrib.auth import get_user_model
from ..models import Contrato
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
# import settings
from django.conf import settings

class ContratoSerializer(serializers.ModelSerializer):
    """serializer for docDriver model"""

    class Meta:
        model = Contrato
        exclude = ("id",)
