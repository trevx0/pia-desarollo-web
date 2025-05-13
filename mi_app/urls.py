from django.contrib import admin
from django.urls import path
from mi_app import views  # Importación correcta desde la app
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Ruta existente
    path('index.html', views.index, name='index_html'),  # Nueva ruta
    path('about/', views.about, name='about'),
    path('contacto/', views.contacto, name='contacto'),
    path('menu-comida.html', views.menu_comida, name='menu_comida'),
    path('menu-bebidas.html', views.menu_bebidas, name='menu_bebidas'),
]