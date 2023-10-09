from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('peliculas/', views.lista_peliculas, name='ultimos_estrenos'),
    path('ficha_pelicula/<id>', views.ficha_pelicula, name='ficha_pelicula')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
