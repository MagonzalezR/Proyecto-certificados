from django.db import models
from django.utils.translation import gettext_lazy as _

# Tipos estaticos
TIPOS_CONTRATO = (
    ("1", "Prestacion de servicios"),
    ("2", "Termino indefinido"),
)

class Contrato(models.Model):
    """Modelo de Contrato"""

    idContrato = models.CharField(_("Identificador del contrato"), max_length=20)
    cedula = models.CharField(_("Cedula del consultor"), max_length=12)
    nombreConsultor = models.CharField(_("Nombre del consultor"), max_length=50)
    idDesarrollo = models.CharField(_("Identificador del contrato en desarrollo"), max_length=10)
    tipoContrato = models.CharField(_("Tipo de contrato"), max_length=50, choices = TIPOS_CONTRATO)
    fechaSuscripcion = models.DateField(_("Fecha de suscripcion"))
    fechaInicio = models.DateField(_("Fecha de inicio"))
    valorContrato = models.PositiveIntegerField(_("Valor del contrato"))
    fechaTerminacion = models.DateField(_("Fecha de terminacion"))

    def __str__(self):
        """Retorna el identificador del contrato"""
        return self.idContrato
