#URLS del la app noticias
from django.urls import include, path

from noticias_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('eventos', views.eventos, name='eventos'),
    path('noticias', views.noticias, name='noticias'),
    path('donaciones', views.donaciones, name='donaciones'),
    path('login', views.login, name='login'),
]