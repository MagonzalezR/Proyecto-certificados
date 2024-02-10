from ..models import Contrato, Otrosi
from ..utils import actualizarOtrosis, actualizarProrrogas
from .serializer import ContratoSerializer, OtrosiSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class ContratosApiView(APIView):
    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk is None:
            # devuelve todos los contratos
            contratos = Contrato.objects.all()
            serializer = ContratoSerializer(contratos, many=True)
            return Response(serializer.data)
        contrato = Contrato.objects.get(pk=pk)
        serializer = ContratoSerializer(contrato)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContratoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, format=None):
        contrato = Contrato.objects.get(id=request.data.get("id"))
        serializer = ContratoSerializer(contrato, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            actualizarOtrosis(contrato.id)
            actualizarProrrogas(contrato.id)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OtrosiApiView(APIView):
    serializer_class = OtrosiSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk is None:
            # devuelve todos los otrosi
            otrosis = Otrosi.objects.all()
            serializer = OtrosiSerializer(otrosis, many=True)
            return Response(serializer.data)
        otrosi = Otrosi.objects.get(pk=pk)
        serializer = OtrosiSerializer(otrosi)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OtrosiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, format=None):
        otrosi = Otrosi.objects.get(id=request.data.get("id"))
        serializer = OtrosiSerializer(otrosi, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            actualizarOtrosis(otrosi.contratoId.id)
            actualizarProrrogas(otrosi.contratoId.id)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)