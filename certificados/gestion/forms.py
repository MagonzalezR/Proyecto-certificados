from django import forms
from .models import Contrato

class ContratoForm(forms.ModelForm):
    
    class Meta:
        model = Contrato
        fields = [
            "idContrato" ,
            "cedula" ,
            "nombreConsultor" ,
            "idDesarrollo" ,
            "tipoContrato" ,
            "fechaSuscripcion" ,
            "fechaInicio" ,
            "valorContrato" ,
            "fechaTerminacion" ,
        ]
        widgets = {
            "idContrato" : forms.TextInput(attrs={"class": "form-control"}),
            "cedula" : forms.TextInput(attrs={"class": "form-control"}),
            "nombreConsultor" : forms.TextInput(attrs={"class": "form-control"}),
            "idDesarrollo" : forms.TextInput(attrs={"class": "form-control"}),
            "tipoContrato" : forms.Select(attrs={"class": "form-control"}),
            "fechaSuscripcion" : forms.DateField(),
            "fechaInicio" : forms.DateField(),
            "valorContrato" : forms.DecimalField(attrs={"class": "form-control"}),
            "fechaTerminacion" : forms.DateField(),
        }
        labels = {
            "idContrato" : "Id del contrato",
            "cedula" : "Cédula del empleado",
            "nombreConsultor" : "Nombre del empleado",
            "idDesarrollo" : "Id del desarrollo",
            "tipoContrato" : "Tipo de contrato",
            "fechaSuscripcion" : "Fecha de suscripción del contrato",
            "fechaInicio" : "Fecha de inicio del contrato",
            "valorContrato" : "Valor del contrato",
            "fechaTerminacion" : "Fecha de terminación del contrato",
        }
    