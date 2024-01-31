from django import forms
from .models import Contrato, Otrosi

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
            "objeto",
            "esSesion",
        ]
        widgets = {
            "idContrato" : forms.TextInput(attrs={"class": "form-control"}),
            "cedula" : forms.TextInput(attrs={"class": "form-control"}),
            "nombreConsultor" : forms.TextInput(attrs = {"class": "form-control"}),
            "idDesarrollo" : forms.TextInput(attrs = {"class": "form-control"}),
            "tipoContrato" : forms.Select( attrs={"class": "form-control"}),
            "fechaSuscripcion" : forms.DateInput(attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
            "fechaInicio" : forms.DateInput(attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
            "valorContrato" : forms.NumberInput(),
            "fechaTerminacion" : forms.DateInput(attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
            "objeto": forms.Textarea(attrs={"class": "form-control"}),
            "esSesion": forms.Select(choices= ((True, "Si"), (False, "No")), attrs={"class": "form-control"}),
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
            "objeto" : "Objeto",
            "esSesion" : "¿Es de sesión?",
            
        }
        