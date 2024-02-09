from .models import Contrato, Otrosi

def actualizarOtrosis(id):
    otrosis = Otrosi.objects.filter(contratoId = id).exclude(deleted=True).order_by('id')
    contrato = Contrato.objects.get(id = id)
    anterior = None
    valorAcumuladoBase = contrato.valorContrato
    for elemento in otrosis:
        if anterior:
            valorAcumuladoBase = anterior.valorAcumulado
        print('valor acumulado: ', valorAcumuladoBase)
        elemento.valorAcumulado= elemento.valorAdicion + valorAcumuladoBase
        elemento.save()
        anterior=elemento

    