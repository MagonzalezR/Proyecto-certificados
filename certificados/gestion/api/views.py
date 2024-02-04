from ..models import Contrato
from .serializer import ContratoSerializer
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
        print(request.data.get("id"), "FLAG")
        contrato = Contrato.objects.get(id=request.data.get("id"))
        serializer = ContratoSerializer(contrato, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ContratoBorrarApi(APIView):
#     serializer_class = ContratoSerializer
#     permission_classes = [IsAuthenticated]
    
#     def post(self)