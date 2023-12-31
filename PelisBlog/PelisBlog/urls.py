"""
URL configuration for PelisBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="inicio"),
    path('peliculas', views.peliculas, name="peliculas"),
    path('login', views.login_succes, name="login"),
    path('logout/', views.logout_succes, name='logout'),
    path('compras/', views.compras, name='compras'),
    path('peliculas/', include('Peliculas.urls')),
    path('registro', views.registro, name="registro"),
    path('orden_de_compra/<id>', views.orden_de_compra, name="orden_de_compra"),
    path('ordenes_de_compras/', views.ordenes_de_compras, name="ordenes_de_compras"),
    path('peril_usario', views.perfil, name='perfil'),
    
    path('reportes/', views.reportes, name="reportes"),
    path('exportar/exportar_reporte_completo/', views.exportar_reporte_completo, name="exportar_reporte_completo"),
    path('exportar/exportar_reporte_fecha/', views.exportar_reporte_fecha, name="exportar_reporte_fecha"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
