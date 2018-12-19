from django.views.generic import TemplateView, CreateView
from proveedor.models import ProveedorServicio, Servicio, Beneficio
from . import models, forms


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proveedores = ProveedorServicio.objects.all()
        context.update(
            proveedores=proveedores,
        )
        return context

class Calendario(TemplateView):
    template_name = 'pagina/calendario.html'



class Proveedor(TemplateView):
    template_name = 'pagina/proveedor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        beneficios = Beneficio.objects.all().values('nombre')
        context.update(
            beneficios=beneficios,
        )
        return context


class FeedbackClientesView(CreateView):
    model = models.FeedBack
    form_class = forms.FeedBackFormCliente
    template_name = 'pagina/feedback-clientes.html'
    success_url = '/'
    def form_valid(self, form):
        object = form.save(commit=True)
        object.tipo = 'CL'
        object.save()
        return super().form_valid(form)


class FeedbackProveedoresView(CreateView):
    model = models.FeedBack
    form_class = forms.FeedBackFormProveedor
    template_name = 'pagina/feedback-proveedores.html'
    success_url = '/'

    def form_valid(self, form):
        object = form.save(commit=True)
        object.tipo = 'PR'
        object.save()
        return super().form_valid(form)