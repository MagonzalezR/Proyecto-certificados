from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from wkhtmltopdf.views import PDFTemplateResponse
from gestion.models import Contrato, Otrosi
from babel.numbers import format_currency
from dateutil import relativedelta
import base64
from django.conf import settings

# Vista base para la consulta y generación de contratos
class VistaConsulta(TemplateView):
    template_name = 'vista_generador.html'

vista_consulta = VistaConsulta.as_view()


# Vista para generar un PDF a partir de un contrato específico (DetailView)
class PDFGeneratorView(DetailView):
    template = 'PDF/content.html'  # Plantilla principal del PDF
    header_template = "PDF/header.html"  # Plantilla para el encabezado
    footer_template = "PDF/footer.html"  # Plantilla para el pie de página
    model = Contrato  # Modelo del que se obtienen los datos

    def get(self, request, *args, **kwargs):
        # Obtener el contrato específico usando su ID
        contrato = Contrato.objects.get(id=self.kwargs["pk"])

        # Obtener los otrosi asociados al contrato
        otrosis = Otrosi.objects.filter(contratoId=contrato).exclude(deleted=True).order_by('id')

        # Formatear la cédula para mejor visualización
        cedula = f"{contrato.cedula[0]}.{contrato.cedula[1:4]}.{contrato.cedula[4:7]}.{contrato.cedula[7:]}"

        # Calcular la diferencia entre fechas de inicio y fin
        fechaDiferencia = relativedelta.relativedelta(contrato.fechaTerminacion, contrato.fechaInicio)

        # Abrir y codificar las imágenes base64 (logotipos y firma)
        with open('./static/img/Logo_Vertical_IDEXUD_Final-1-3-1.png', 'rb') as image_file:
            logoIdexud = base64.b64encode(image_file.read()).decode('utf-8')
        with open('./static/img/EscudoUD.png', 'rb') as image_file:
            logoUd = base64.b64encode(image_file.read()).decode('utf-8')
        with open('./static/img/Firma.png', 'rb') as image_file:
            firma = base64.b64encode(image_file.read()).decode('utf-8')

        # Preparar el contexto para el template del PDF
        context = {
            'contrato': contrato,
            'otrosis': otrosis,
            'cedula': cedula,
            'valorC': format_currency(contrato.valorContrato, 'COP', locale='es'),  # Formatear valor a moneda
            'DifFechas': fechaDiferencia,
            'logoIdexud': logoIdexud,
            'logoUd': logoUd,
            'firma': firma,
        }

        # Opciones para la generación del PDF
        options = {
            'images': True,  # Habilitar imágenes
            'enable-external-links': True,  # Habilitar enlaces externos
            'print-media-type': True,  # Imprimir en modo "media"
            'enable-internal-links': True,  # Habilitar enlaces internos
            'enable-local-file-access': True,  # Permitir acceso a archivos locales
        }

        # Generar la respuesta PDF
        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       header_template=self.header_template,
                                       footer_template=self.footer_template,
                                       filename=f"Contrato-{contrato.idContrato}-{contrato.nombreConsultor}-{contrato.fechaInicio.strftime('%Y %m %d')}.pdf",   # Nombre con el que se mostratra el archivo
                                       context=context,
                                       show_content_in_browser=True,  # Mostrar contenido en el navegador
                                       cmd_options=options)

        return response


vista_PDF = PDFGeneratorView.as_view()