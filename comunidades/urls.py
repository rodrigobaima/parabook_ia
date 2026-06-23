from django.urls import path
from .views import (
    comunidade_list,
    comunidade_detail,
    comunidade_create,
    comunidade_update,
    comunidade_delete,
    acesso_comunidade,
    conteudo_comunidade
)

app_name = 'comunidades'

urlpatterns = [
    # GET /comunidades/ - List all communities
    path('', comunidade_list, name='list'),
    
    # GET /comunidades/<id>/ - Detail view of a community
    path('<int:id>/', comunidade_detail, name='detail'),
    
    # POST /comunidades/create/ - Create new community
    path('create/', comunidade_create, name='create'),
    
    # POST /comunidades/<id>/edit/ - Update community
    path('<int:id>/edit/', comunidade_update, name='update'),
    
    # POST /comunidades/<id>/delete/ - Delete community
    path('<int:id>/delete/', comunidade_delete, name='delete'),
    
    # Legacy routes for backward compatibility with existing templates
    path('acesso/', acesso_comunidade, name='acesso_comunidade'),
    path('conteudo/', conteudo_comunidade, name='conteudo_comunidade'),
]