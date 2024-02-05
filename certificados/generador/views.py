from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from wkhtmltopdf.views import PDFTemplateResponse
from gestion.models import Contrato, Otrosi
from babel.numbers import format_currency
from dateutil import relativedelta


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
        otrosis = Otrosi.objects.filter(contratoId=contrato)
        cedula = contrato.cedula[0]+'.'+contrato.cedula[1:4] +"."+contrato.cedula[4:7]+"."+contrato.cedula[7:]
        fechaDiferencia = relativedelta.relativedelta(contrato.fechaTerminacion, contrato.fechaInicio)
        context = {'contrato': contrato,
                   'otrosis': otrosis,
                   'cedula': cedula, 
                   'valorC': format_currency(contrato.valorContrato, 'COP', locale='es'),
                   'DifFechas': fechaDiferencia}

        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       header_template=self.header_template,
                                       footer_template=self.footer_template,
                                       filename="Contrato-"+contrato.idContrato+"-"+contrato.nombreConsultor+"-"+contrato.fechaInicio.strftime("%Y %m %d")+".pdf",
                                       context=context,
                                       show_content_in_browser=False,
                                       )
        return response


vista_PDF = PDFGeneratorView.as_view()
