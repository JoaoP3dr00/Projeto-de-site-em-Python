from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


# O dicionário criado foi pra passar um dado de nome para o view
# e ser exibido na tela, mas precisa anotar no arquivo html do index
# com {{ nome }}
# a chave e o valor contatos é referente aos valores adicionados na área admin,
# então eles serão exibidos na home
def index(request):
    contatos = Contato.objects.order_by('-id').filter(mostrar=True)  # ordena os valores pelo id em ordem decrescente
    # Olhar a documentação do django para mais opções "django documentation filter"
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)  # redefinindo as lista de contatos para os 10 definidos em paginator

    return render(request, 'contatos/index.html', {"contatos": contatos, "nome": "João Pedro"})


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404  # Raise http404 usado para lançar uma exceção de dentro do método e suspender os outros códigos

    return render(request, 'contatos/ver_contato.html', {"contato": contato})


def busca(request):
    termo = request.GET.get("termo")

    if termo is None or not termo:
        return redirect('index')  # para redirecionar o usuário para o url da página principal novamente

    campos = Concat('nome', Value(' '), 'sobrenome')
    # campos é a junção do nome e sobrenome, para o caso onde a pesquisa é feita com o nome completo
    # da pessoa, e Value(' ') simula um campo que não existe nos nossos modelos para ajudar na concatenação

    contatos = Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo))
    # Para realizar a pesquisa nos valores em que o nome completo OU o telefone são iguais ao termo utilizando
    # utilizando "| - pipe"

    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {"contatos": contatos, "nome": "João Pedro"})
