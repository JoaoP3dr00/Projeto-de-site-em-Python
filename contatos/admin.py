from django.contrib import admin
from .models import Categoria, Contato


# Classe usada para mostrar os outros campos
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')  # Usado para permitir clicar em cima dos campos
    list_filter = ('nome', 'sobrenome')  # Usado para filtrar pelos campos
    list_per_page = 10  # Quantidades de elementos por página para serem exibidos
    search_fields = ('nome', 'sobrenom', 'telefone')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

