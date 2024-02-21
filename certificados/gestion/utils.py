from .models import Contrato, Otrosi
from dateutil import relativedelta

def actualizarOtrosis(id):
    """
    Actualiza el valor acumulado de los otrosíes asociados a un contrato.

    Args:
        id: El ID del contrato.
    """

    otrosis = Otrosi.objects.filter(contratoId=id).exclude(deleted=True).order_by('id')
    contrato = Contrato.objects.get(id=id)
    anterior = None
    valorAcumuladoBase = contrato.valorContrato

    for elemento in otrosis:
        if anterior:
            valorAcumuladoBase = anterior.valorAcumulado

        elemento.valorAcumulado = elemento.valorAdicion + valorAcumuladoBase
        elemento.save()
        anterior = elemento

def actualizarProrrogas(id):
    """
    Actualiza la prórroga de los otrosíes asociados a un contrato.

    Args:
        id: El ID del contrato.
    """

    otrosis = Otrosi.objects.filter(contratoId=id).exclude(deleted=True).order_by('fechaTerminacionOtrosi')
    contrato = Contrato.objects.get(id=id)
    anterior = None

    for elemento in otrosis:
        if anterior:
            elemento.prorroga = calcular_prorroga(anterior.fechaTerminacionOtrosi, elemento.fechaTerminacionOtrosi)
        else:
            elemento.prorroga = calcular_prorroga(contrato.fechaTerminacion, elemento.fechaTerminacionOtrosi)

        elemento.save()
        anterior = elemento

def calcular_prorroga(fecha_inicio, fecha_fin):
    """
    Calcula la prórroga entre dos fechas.

    Args:
        fecha_inicio: La fecha de inicio.
        fecha_fin: La fecha de fin.

    Returns:
        Un string con la diferencia en días, meses y años.
    """

    diferencia_dias = relativedelta.relativedelta(fecha_fin, fecha_inicio)
    if( diferencia_dias.days<0 or diferencia_dias.months <0 or diferencia_dias.years<0):
        return "0"
    return f" {diferencia_dias.days} días, {diferencia_dias.months} meses, {diferencia_dias.years} años"

