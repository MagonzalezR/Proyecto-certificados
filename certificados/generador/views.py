from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from wkhtmltopdf.views import PDFTemplateResponse 
from gestion.models import Contrato, Otrosi

class VistaConsulta(TemplateView):
    template_name = 'vista_generador.html'

vista_consulta = VistaConsulta.as_view()

class PDFGeneratorView(DetailView):
    template='PDF/content.html'
    header_template = "PDF/header.html"
    footer_template = "PDF/footer.html"
    context= {'title': 'Hello World!', 'header':'header', 'footer':'footer'}
    model = Contrato

    def get(self, request, *args, **kwargs):
        # self.context['book'] = self.get_object()
        print(self.context)
        
        response=PDFTemplateResponse(request=request,
                                     template=self.template,
                                     header_template=self.header_template,
                                     footer_template=self.footer_template,
                                     filename ="hello.pdf",
                                     context=self.context,
                                     show_content_in_browser=True,
                                     )
        return response
vista_PDF = PDFGeneratorView.as_view()
