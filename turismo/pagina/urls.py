from django.urls import path
from . import views


app_name = 'pagina'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('calendario/', views.Calendario.as_view(), name='calendario'),
    path('proveedor/', views.Proveedor.as_view(), name='proveedor'),
    path('feedback/clientes/', views.FeedbackClientesView.as_view(), name='feedback-clientes'),
    path('feedback/proveedores/', views.FeedbackProveedoresView.as_view(), name='feedback-proveedores'),

]