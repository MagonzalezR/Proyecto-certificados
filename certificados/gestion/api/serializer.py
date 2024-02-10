from django.contrib.auth import get_user_model
from ..models import Contrato, Otrosi
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
# import settings
from django.conf import settings

class ContratoSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Contrato."""

    # Opcionalmente, puedes agregar campos personalizados o modificar la representación de campos existentes:
    # nombre_completo = serializers.SerializerMethodField()
    # def get_nombre_completo(self, obj):
    #     return f"{obj.nombre} {obj.apellido}"

    class Meta:
        model = Contrato
        fields = '__all__'  # Incluye todos los campos del modelo


class OtrosiSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Otrosi."""

    class Meta:
        model = Otrosi
        fields = '__all__'  # Incluye todos los campos del modelo
