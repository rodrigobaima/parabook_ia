from django.shortcuts import render, redirect, get_object_or_404
from .models import Comunidade


# Renamed from 'comunidades' for RESTful convention
def comunidade_list(request):
    """GET /comunidades/ - List all communities"""
    lista_comunidades = Comunidade.objects.all()

    return render(request, 'comunidades/comunidade.html', {
        'comunidades': lista_comunidades
    })


def comunidade_detail(request, id):
    """GET /comunidades/<id>/ - Detail view of a community"""
    comunidade = get_object_or_404(Comunidade, id=id)
    return render(request, 'comunidades/card-comunidade.html', {
        'comunidade': comunidade
    })


# Renamed from 'criar_comunidade' for RESTful convention
def comunidade_create(request):
    """POST /comunidades/create/ - Create new community"""
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')

        Comunidade.objects.create(
            nome=nome,
            descricao=descricao
        )

        return redirect('comunidades:list')

    return render(request, 'comunidades/criar-comunidade.html')


# Renamed from 'editar_comunidade' for RESTful convention
def comunidade_update(request, id):
    """POST /comunidades/<id>/edit/ - Update community"""
    comunidade = get_object_or_404(Comunidade, id=id)

    if request.method == 'POST':
        comunidade.nome = request.POST.get('nome')
        comunidade.descricao = request.POST.get('descricao')
        comunidade.save()

        return redirect('comunidades:list')

    return render(request, 'comunidades/editar-comunidade.html', {
        'comunidade': comunidade
    })


# Renamed from 'excluir_comunidade' for RESTful convention
def comunidade_delete(request, id):
    """POST /comunidades/<id>/delete/ - Delete community"""
    comunidade = get_object_or_404(Comunidade, id=id)

    if request.method == 'POST':
        comunidade.delete()
        return redirect('comunidades:list')

    return render(request, 'comunidades/excluir-comunidade.html', {
        'comunidade': comunidade
    })


# Legacy views - kept for backward compatibility
def acesso_comunidade(request):
    return render(request, 'comunidades/acesso-comunidade.html')


def conteudo_comunidade(request):
    return render(request, 'comunidades/conteudo-comunidade.html')