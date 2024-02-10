from .models import Contrato, Otrosi
from dateutil import relativedelta

def actualizarOtrosis(id):
    otrosis = Otrosi.objects.filter(contratoId = id).exclude(deleted=True).order_by('id')
    contrato = Contrato.objects.get(id = id)
    anterior = None
    valorAcumuladoBase = contrato.valorContrato
    for elemento in otrosis:
        if anterior:
            valorAcumuladoBase = anterior.valorAcumulado
        elemento.valorAcumulado= elemento.valorAdicion + valorAcumuladoBase
        elemento.save()
        anterior=elemento

def actualizarProrrogas(id):
    otrosis = Otrosi.objects.filter(contratoId = id).exclude(deleted=True).order_by('fechaTerminacionOtrosi')
    contrato = Contrato.objects.get(id = id)
    anterior = None
    for elemento in otrosis:
        if anterior:
            elemento.prorroga= calcular_prorroga(anterior.fechaTerminacionOtrosi, elemento.fechaTerminacionOtrosi)
        else:
            elemento.prorroga= calcular_prorroga(contrato.fechaTerminacion, elemento.fechaTerminacionOtrosi)
        elemento.save()
        anterior=elemento

def calcular_prorroga(fecha_inicio, fecha_fin):
  diferencia_dias = relativedelta.relativedelta(fecha_fin,fecha_inicio)
  return f" {diferencia_dias.days} días, {diferencia_dias.months} meses, {diferencia_dias.years} años"
     