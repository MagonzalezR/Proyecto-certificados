from django import forms
from .models import Contrato, Otrosi


class ContratoForm(forms.ModelForm):

    """Formulario para la creación y edición de Contratos."""
    class Meta:
        model = Contrato    #Modelo asociado
        fields = [          #Campos que se quieren mostrar (asociados al modelo)
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
            "observaciones",
            "correo",
            "telefono",
            "direccion",
        ]
        widgets = {     #Como se carga cada campo en el template
            "idContrato": forms.TextInput(attrs={"class": "form-control", 'placeholder': '0000 X 20XX'}),
            "cedula": forms.TextInput(attrs={"class": "form-control", 'placeholder': '123456789', 'pattern':"^\d{6,11}$",'title':'Deben ser números entre 6 y 11 caracteres'}),
            "nombreConsultor": forms.TextInput(attrs={"class": "form-control",'placeholder': 'Nombre y apellido','pattern':'^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$', 'title':'se aceptan letras y espacios, pueden llevar acentos.'}),
            "correo": forms.TextInput(attrs={"class": "form-control", "placeholder":"Correo@ejemplo.com", 'pattern':'[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{2,5}','title':'Debe ser del formato nombre@correo.com'}),
            "telefono": forms.TextInput(attrs={"class": "form-control", "placeholder":"312123456", 'pattern':'[\(]?[\+]?(\d{2}|\d{3})[\)]?[\s]?(\d{6}|\d{8}|\d{10}|\d{12}|\d{3}[\*\.\-]{2}\d{3}|\d{2}[\*\.\-\s]{3}\d{2}|\d{4}[\*\.\-\s]\d{4})','title':'Deben ser del formato +57 3112223334'}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "placeholder":"Calle 1 # 1-1"}),
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
        labels = {      #Label asociado a cada campo
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
            "correo": "Correo",
            "telefono": "Teléfono",
            "direccion": "Dirección",
        }
        
    def clean(self):        #Aqui van los validadores individuales que se deseen agregar
        cleaned_data = super().clean()
        return cleaned_data
        


class OtrosiForm(forms.ModelForm):
    
    """Formulario para la creación y edición de Otrosi ."""
    class Meta:
        model = Otrosi          #Modelo asociado

        fields = [              #Campos que se quieren mostrar (asociados al modelo)
            "valorAdicion",
            "fechaTerminacionOtrosi",
            "observaciones",
        ]

        widgets = {              #Como se carga cada campo en el template
            "valorAdicion": forms.NumberInput(),
            "fechaTerminacionOtrosi": forms.DateInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Select a date',
                                                             'type': 'date'
                                                             }, format=('%Y-%m-%d')),
            "observaciones": forms.Textarea(attrs={"class": "form-control", "rows": "4"}),
        }

        labels = {
            "valorAdicion": "Valor de la adición",
            "fechaTerminacionOtrosi": "Fecha de terminación de la adición",
            "observaciones": "Observaciones",
        }
