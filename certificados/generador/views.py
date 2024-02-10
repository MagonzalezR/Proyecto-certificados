from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from wkhtmltopdf.views import PDFTemplateResponse
from gestion.models import Contrato, Otrosi
from babel.numbers import format_currency
from dateutil import relativedelta
import base64
from django.conf import settings

class VistaConsulta(TemplateView):
    template_name = 'vista_generador.html'


vista_consulta = VistaConsulta.as_view()


class PDFGeneratorView(DetailView):
    template = 'PDF/content.html'
    header_template = "PDF/header.html"
    footer_template = "PDF/footer.html"
    model = Contrato

    def get(self, request, *args, **kwargs):
        contrato = Contrato.objects.get(id=self.kwargs["pk"])       #Se obtiene el contrato que se va a mostrar
        otrosis = Otrosi.objects.filter(contratoId=contrato).exclude(deleted=True).order_by('id')
        cedula = contrato.cedula[0]+'.'+contrato.cedula[1:4] +"."+contrato.cedula[4:7]+"."+contrato.cedula[7:]
        fechaDiferencia = relativedelta.relativedelta(contrato.fechaTerminacion, contrato.fechaInicio)
        with open('./static/img/Logo_Vertical_IDEXUD_Final-1-3-1.png', 'rb') as image_file:
            logoIdexud = base64.b64encode(image_file.read()).decode('utf-8')
        with open('./static/img/EscudoUD.png', 'rb') as image_file:
            logoUd = base64.b64encode(image_file.read()).decode('utf-8')
        with open('./static/img/Firma.png', 'rb') as image_file:
            firma = base64.b64encode(image_file.read()).decode('utf-8')
        context = {'contrato': contrato,
                   'otrosis': otrosis,
                   'cedula': cedula, 
                   'valorC': format_currency(contrato.valorContrato, 'COP', locale='es'),
                   'DifFechas': fechaDiferencia,
                   'logoIdexud': logoIdexud,
                   'logoUd': logoUd,
                   'firma': firma}
        options={'images': True, 'enable-external-links': True, 'print-media-type': True,'enable-internal-links': True, 'enable-local-file-access': True}
        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       header_template=self.header_template,
                                       footer_template=self.footer_template,
                                       filename="Contrato-"+contrato.idContrato+"-"+contrato.nombreConsultor+"-"+contrato.fechaInicio.strftime("%Y %m %d")+".pdf",
                                       context=context,
                                       show_content_in_browser=True,
                                       cmd_options= options
                                       )
        return response


vista_PDF = PDFGeneratorView.as_view()
