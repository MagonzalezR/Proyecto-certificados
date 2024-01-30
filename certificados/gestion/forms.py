from django import forms
from .models import Contrato, Actividad, Objeto, Otrosi

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
            "objetoId",
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
            "objetoId": forms.Select(choices = Objeto.objects.all() , attrs={"class": "form-control"}),
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
            "objetoId" : "Objeto",
            "esSesion" : "¿Es de sesión?",
            
        }
    
        
class ObjetoForm(forms.ModelForm):
    
    class Meta:
        model = Objeto
        
        fields = [
            "nombreObjeto",
            "descripcionObjeto",
        ]
        
        widgets = {
            "nombreObjeto" : forms.TextInput(attrs={"class": "form-control"}) ,
            "descripcionObjeto" : forms.Textarea(attrs={"class": "form-control"}) ,
        }
        
        labels = {
            "nombreObjeto": "Nombre del objeto",
            "descripcionObjeto": "Descripción del objeto",
        }

class ActividadForm(forms.ModelForm):
    
    class Meta:
        model = Actividad
        
        fields = [
            "nombreActividad",
            "descripcionActividad", 
        ]
        
        widgets = {
            "nombreActividad" : forms.TextInput(attrs={"class": "form-control"}) ,
            "descripcionActividad" : forms.Textarea(attrs={"class": "form-control"}) ,
        }
        
        labels = {
            "nombreActividad" : "Nombre de la actividad",
            "descripcionActividad" : "Descripción de la actividad", 
        }
        