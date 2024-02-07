from django import forms
from .models import Contrato, Otrosi


class ContratoForm(forms.ModelForm):

    class Meta:
        model = Contrato
        fields = [
            "idContrato",
            "cedula",
            "nombreConsultor",
            "idDesarrollo",
            "tipoContrato",
            "fechaSuscripcion",
            "fechaInicio",
            "valorContrato",
            "fechaTerminacion",
            "objeto",
            "esSesion",
            "fechaSesion",
            "infoSesion",
            "observaciones"
        ]
        widgets = {
            "idContrato": forms.TextInput(attrs={"class": "form-control", 'placeholder': '0000 X 20XX'}),
            "cedula": forms.TextInput(attrs={"class": "form-control", 'placeholder': '123456789', 'pattern':"^\d{6,11}$",'title':'Deben ser números entre 6 y 11 caracteres'}),
            "nombreConsultor": forms.TextInput(attrs={"class": "form-control",'placeholder': 'Nombre y apellido','pattern':'^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$', 'title':'se aceptan letras y espacios, pueden llevar acentos.'}),
            "idDesarrollo": forms.TextInput(attrs={"class": "form-control",'placeholder': '0000-20XX'}),
            "tipoContrato": forms.Select(attrs={"class": "form-control"}),
            "fechaSuscripcion": forms.DateInput(attrs={'class': 'form-control',
                                                       'type': 'date', 'onchange': 'clickFechaSesion("id_fechaInicio","id_fechaSuscripcion")'
                                                       }, format=('%Y-%m-%d')),
            "fechaInicio": forms.DateInput(attrs={'class': 'form-control',
                                                  'type': 'date', 'disabled':'true', 'onchange': 'clickFechaSesion("id_fechaTerminacion","id_fechaInicio")'
                                                  }, format=('%Y-%m-%d')),
            "valorContrato": forms.NumberInput(attrs={'placeholder': '1000111'}),
            "fechaTerminacion": forms.DateInput(attrs={'class': 'form-control',
                                                       'type': 'date', 'disabled':'true'
                                                       }, format=('%Y-%m-%d')),
            "objeto": forms.Textarea(attrs={"class": "form-control", "rows": "4"}),
            "esSesion": forms.Select(choices=((False, "No"), (True, "Si")) , attrs={"class": "form-control","onchange":"mostrar()"}),
            "fechaSesion": forms.DateInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Select a date',
                                                       'type': 'date'
                                                       }, format=('%Y-%m-%d')),
            "infoSesion": forms.TextInput(attrs={"class": "form-control"}),
            "observaciones": forms.Textarea(attrs={"class": "form-control", "rows": "4"}),
        }
        labels = {
            "idContrato": "Id del contrato",
            "cedula": "Cédula del empleado",
            "nombreConsultor": "Nombre del empleado",
            "idDesarrollo": "Id del desarrollo",
            "tipoContrato": "Tipo de contrato",
            "fechaSuscripcion": "Fecha de suscripción del contrato",
            "fechaInicio": "Fecha de inicio del contrato",
            "valorContrato": "Valor del contrato",
            "fechaTerminacion": "Fecha de terminación del contrato",
            "objeto": "Objeto",
            "esSesion": "¿Es de cesión?",
            "fechaSesion": "Fecha de la cesión",
            "infoSesion": "Información de cesión",
            "observaciones": "Observaciones",

        }
        
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
        


class OtrosiForm(forms.ModelForm):
    class Meta:
        model = Otrosi

        fields = [
            "valorAdicion",
            "prorroga",
            "fechaTerminacionOtrosi",
            "observaciones",
        ]

        widgets = {
            "valorAdicion": forms.NumberInput(),
            "prorroga": forms.NumberInput(),
            "fechaTerminacionOtrosi": forms.DateInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Select a date',
                                                             'type': 'date'
                                                             }),
            "observaciones": forms.Textarea(attrs={"class": "form-control", "rows": "4"}),
        }

        labels = {
            "valorAdicion": "Valor de la adición",
            "prorroga": "Tiempo de la prorroga (en meses)",
            "fechaTerminacionOtrosi": "Fecha de terminación de la adición",
            "observaciones": "Observaciones",
        }
