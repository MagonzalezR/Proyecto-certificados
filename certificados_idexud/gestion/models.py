from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from base64 import b64encode

# Tipos estaticos
TIPOS_CONTRATO = (
    ("8", 'Contrato de Prestación de servicios'),
    ("1", "Contrato Indefinido"),
    ("2", "Contrato por Obra o Labor"),
    ("3", 'Contrato Eventual'),
    ("4", 'Contrato de Interinidad'),
    ("5", 'Contrato de Relevo'),
    ("6", 'Contrato de Formación y aprendizaje'),
    ("7", 'Contrato de Prácticas'),
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
    objeto = models.CharField(_("Objeto"), max_length=1000)
    actividades = ArrayField(models.CharField(max_length=1000))
    esSesion = models.BooleanField(_("¿El contrato es de sesión?"))
    fechaSesion = models.DateField(_("Fecha de la sesión"), null = True, blank = True)
    infoSesion = models.CharField(_("Info de la sesión"), null = True, blank = True)
    observaciones = models.CharField(_("Observaciones"), max_length=1000, null = True, blank = True)
    correo = models.CharField(_("Correo electrónico"))
    telefono = models.CharField(_("Teléfono"), max_length = 14)
    direccion = models.CharField(_("Dirección"))
    codigo = models.CharField(_("SC"))
    deleted = models.BooleanField(default=False)

    def __str__(self):
        """Retorna el identificador del contrato"""
        return self.idContrato + " - " +str(self.id)
    
    def save(self, *args, **kwargs):
        self.codigo = self.generar_campo_base64()
        super().save(*args, **kwargs)
    
    def generar_campo_base64(self):
        valor_concatenado = f"{self.cedula}{self.nombreConsultor}{self.idContrato}{self.correo}{self.telefono}"
        valor_base64 = b64encode(valor_concatenado.encode()).decode()
        return valor_base64

class Otrosi(models.Model):
    """Modelo de Otrosis"""

    valorAdicion = models.PositiveIntegerField(_("Valor de adición"))
    prorroga = models.CharField(_("Prorroga (d-m-y)"))
    fechaTerminacionOtrosi = models.DateField(_("Fecha de terminación del otrosi"))
    valorAcumulado = models.PositiveIntegerField(_("Prorroga (en meses)"))
    contratoId = models.ForeignKey(Contrato, on_delete = models.CASCADE, null = True)
    actividades = ArrayField(models.CharField(max_length=1000))
    observaciones = models.CharField(_("Observaciones"), max_length=1000, null = True, blank = True)
    deleted = models.BooleanField(default=False)
    