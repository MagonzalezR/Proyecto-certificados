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
            "observaciones"
        ]
        widgets = {
            "idContrato": forms.TextInput(attrs={"class": "form-control"}),
            "cedula": forms.TextInput(attrs={"class": "form-control"}),
            "nombreConsultor": forms.TextInput(attrs={"class": "form-control"}),
            "idDesarrollo": forms.TextInput(attrs={"class": "form-control"}),
            "tipoContrato": forms.Select(attrs={"class": "form-control"}),
            "fechaSuscripcion": forms.DateInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Select a date',
                                                       'type': 'date'
                                                       }),
            "fechaInicio": forms.DateInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Select a date',
                                                  'type': 'date'
                                                  }),
            "valorContrato": forms.NumberInput(),
            "fechaTerminacion": forms.DateInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Select a date',
                                                       'type': 'date'
                                                       }),
            "objeto": forms.Textarea(attrs={"class": "form-control", "rows": "4"}),
            "esSesion": forms.Select(choices=((False, "No"), (True, "Si")) , attrs={"class": "form-control","onchange":"mostrar()"}),
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
            "esSesion": "¿Es de sesión?",
            "observaciones": "Observaciones",

        }


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
