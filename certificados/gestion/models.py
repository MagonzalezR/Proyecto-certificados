from django.db import models
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

class Objeto(models.Model):
    """Modelo de Objetos"""
    
    nombreObjeto = models.CharField(_("Nombre del objeto"), max_length=20)
    descripcionObjeto = models.CharField(_("Descripción del objeto"), max_length=255)
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
         """Retorna el nombre del Objeto"""
         return self.nombreObjeto
    

class Actividad(models.Model):
    """Modelo de Actividades"""
    
    nombreActividad = models.CharField(_("Nombre de la actividad"), max_length=20)
    descripcionActividad = models.CharField(_("Descripción del actividad"), max_length=255)
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
         """Retorna el nombre del Objeto"""
         return self.nombreActividad + str(self.id)

class Contrato(models.Model):
    """Modelo de Contrato"""

    idContrato = models.CharField(_("Identificador del contrato"), max_length=20)
    cedula = models.CharField(_("Cédula del consultor"), max_length=12)
    nombreConsultor = models.CharField(_("Nombre del consultor"), max_length=50)
    idDesarrollo = models.CharField(_("Identificador del contrato en desarrollo"), max_length=10)
    tipoContrato = models.CharField(_("Tipo de contrato"), max_length=50, choices = TIPOS_CONTRATO)
    fechaSuscripcion = models.DateField(_("Fecha de suscripción"))
    fechaInicio = models.DateField(_("Fecha de inicio"))
    valorContrato = models.PositiveIntegerField(_("Valor del contrato"))
    fechaTerminacion = models.DateField(_("Fecha de terminación"))
    objetoId = models.ForeignKey(Objeto, on_delete = models.CASCADE, null = True)
    actividadesIds = models.ManyToManyField(Actividad)
    esSesion = models.BooleanField(_("¿El contrato es de sesión?"))
    deleted = models.BooleanField(default=False)

    def __str__(self):
        """Retorna el identificador del contrato"""
        return self.idContrato

class Otrosi(models.Model):
    """Modelo de Otrosis"""

    valorAdicion = models.PositiveIntegerField(_("Valor de adición"))
    prorroga = models.PositiveIntegerField(_("Prorroga (en meses)"))
    fechaTerminacionOtrosi = models.DateField(_("Fecha de terminación del otrosi"))
    valorAcumulado = models.PositiveIntegerField(_("Prorroga (en meses)"))
    contratoId = models.ForeignKey(Contrato, on_delete = models.CASCADE, null = True)
    actividadesIds = models.ManyToManyField(Actividad)
    deleted = models.BooleanField(default=False)
    