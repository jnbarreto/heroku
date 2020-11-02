from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import lista_equipamentos, novo_equipamento, atualizar_equipamento, deleta_equipamento

urlpatterns = [

    path('lista/', lista_equipamentos, name='lista'),
    path('novo/', novo_equipamento, name='novo_equipamento'),
    path('atualizar/<int:id>/', atualizar_equipamento, name='atualizar_equipamento'),
    path('deleta/<int:id>/', deleta_equipamento, name='deleta_equipamento')
]