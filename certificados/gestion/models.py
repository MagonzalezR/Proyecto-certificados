from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

# Tipos estaticos
TIPOS_CONTRATO = (
    ("1", "Prestación de servicios"),
    ("2", "Termino indefinido"),
    ("3", 'Contrato Indefinido'),
    ("4", 'Contrato Temporal'),
    ("5", 'Contrato en Prácticas'),
    ("6", 'Contrato de Formación'),
    ("7", 'Contrato de prestación de servicios'),
)

class Contrato(models.Model):
    """Modelo de Contrato"""

    idContrato = models.CharField(_("Identificador del contrato"), max_length=20)
    cedula = models.CharField(_("Cédula del consultor"), max_length=12)
    nombreConsultor = models.CharField(_("Nombre del consultor"), max_length=50)
    idDesarrollo = models.CharField(_("Identificador del contrato en desarrollo"), max_length=10)
    tipoContrato = models.CharField(_("Tipo de contrato"), choices = TIPOS_CONTRATO)
    fechaSuscripcion = models.DateField(_("Fecha de suscripción"))
    fechaInicio = models.DateField(_("Fecha de inicio"))
    valorContrato = models.PositiveIntegerField(_("Valor del contrato"))
    fechaTerminacion = models.DateField(_("Fecha de terminación"))
    objeto = models.CharField(_("Objeto"), max_length=600)
    actividades = ArrayField(models.CharField(max_length=600))
    esSesion = models.BooleanField(_("¿El contrato es de sesión?"))
    fechaSesion = models.DateField(_("Fecha de la sesión"), null = True, blank = True)
    infoSesion = models.CharField(_("Info de la sesión"), null = True, blank = True)
    observaciones = models.CharField(_("Observaciones"), max_length=600, null = True, blank = True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        """Retorna el identificador del contrato"""
        return self.idContrato + " - " +str(self.id)

class Otrosi(models.Model):
    """Modelo de Otrosis"""

    valorAdicion = models.PositiveIntegerField(_("Valor de adición"))
    prorroga = models.PositiveIntegerField(_("Prorroga (en meses)"))
    fechaTerminacionOtrosi = models.DateField(_("Fecha de terminación del otrosi"))
    valorAcumulado = models.PositiveIntegerField(_("Prorroga (en meses)"))
    contratoId = models.ForeignKey(Contrato, on_delete = models.CASCADE, null = True)
    actividades = ArrayField(models.CharField(max_length=600))
    observaciones = models.CharField(_("Observaciones"), max_length=300, null = True, blank = True)
    deleted = models.BooleanField(default=False)
    