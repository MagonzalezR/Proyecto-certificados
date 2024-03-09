from ..models import Contrato, Otrosi
from ..utils import actualizarOtrosis, actualizarProrrogas
from .serializer import ContratoSerializer, OtrosiSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class ContratosApiView(APIView):
    """Vista API para la gestión de contratos."""

    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def get(self, request, pk=None, format=None):
        """
        - Obtener todos los contratos (GET /contratos/)
        - Obtener un contrato específico (GET /contratos/<pk>/)
        """
        if pk is None:
            # Obtener todos los contratos
            contratos = Contrato.objects.all()
            serializer = ContratoSerializer(contratos, many=True)
            return Response(serializer.data)
        else:
            # Obtener un contrato específico
            contrato = Contrato.objects.get(pk=pk)
            serializer = ContratoSerializer(contrato)
            return Response(serializer.data)

    def post(self, request, format=None):
        """
        Crear un nuevo contrato (POST /contratos/)
        """
        serializer = ContratoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        """
        Actualizar parcialmente un contrato existente (PATCH /contratos/<pk>/)
        - Actualizar y recalcular otrosí y prórrogas del contrato.
        """
        contrato = Contrato.objects.get(id=request.data.get("id"))
        serializer = ContratoSerializer(contrato, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            actualizarOtrosis(contrato.id)
            actualizarProrrogas(contrato.id)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OtrosiApiView(APIView):
    """Vista API para la gestión de otrosi."""

    serializer_class = OtrosiSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def get(self, request, pk=None, format=None):
        """
        - Obtener todos los otrosi (GET /otrosi/)
        - Obtener un otrosi específico (GET /otrosi/<pk>/)
        """
        if pk is None:
            # Obtener todos los otrosi
            otrosis = Otrosi.objects.all()
            serializer = OtrosiSerializer(otrosis, many=True)
            return Response(serializer.data)
        else:
            # Obtener un otrosi específico
            otrosi = Otrosi.objects.get(pk=pk)
            serializer = OtrosiSerializer(otrosi)
            return Response(serializer.data)

    def post(self, request, format=None):
        """
        Crear un nuevo otrosi (POST /otrosi/)
        """
        serializer = OtrosiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        """
        Actualizar parcialmente un otrosi existente (PATCH /otrosi/<pk>/)
        - Actualizar y recalcular otrosí y prórrogas del contrato asociado.
        """
        otrosi = Otrosi.objects.get(id=request.data.get("id"))
        serializer = OtrosiSerializer(otrosi, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            actualizarOtrosis(otrosi.contratoId.id)
            actualizarProrrogas(otrosi.contratoId.id)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
