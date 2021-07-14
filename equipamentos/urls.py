from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from equipamentos import urls as equip_urls
from .views import ListEquipamentos, NewEquipamento, UpdateEquipamento
from .views import DetailEquipamentos, DeleteEquipamento
urlpatterns = [

    path('list/', ListEquipamentos.as_view(), name='list'),
    path('detail/<int:pk>/', DetailEquipamentos.as_view(), name='detail'),
    path('new/', NewEquipamento.as_view(), name='new'),
    path('update/<int:pk>', UpdateEquipamento.as_view(), name='update'),
    path('delete/<int:pk>', DeleteEquipamento.as_view(), name='delete')
]