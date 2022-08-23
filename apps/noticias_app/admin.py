from django.contrib import admin
from .models import Categoria,Noticia,Comentario
from django.utils.safestring import mark_safe


# Register your models here.
#admin.site.register(Categoria)
#admin.site.register(Noticia)
#admin.site.register(Comentario)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Categoria,CategoriaAdmin)

class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor', 'img')
    search_fields = ('titulo','autor', 'creado')

    list_per_page = 25
#Lo comento porque me da error y llama readonly_fields
    #readonly_fields = ['noticia_img'] 

    def noticias_img(self, obj):
        return mark_safe(
            '<a href="{0}"><img src="{0}" with="30%"></a>'.format(self.img.url)
        )
admin.site.register(Noticia, NoticiasAdmin) 

class ComentariosAdmin(admin.ModelAdmin):

    #list_display =('comentario','cuerpo_comentario','noticia','creado','aprobado') #no existe campo comentario
    list_display =('autor','cuerpo_comentario','noticia','creado','aprobado')
    
    list_filter = ('aprobado','creado')

    search_fields = ('autor', 'cuerpo_comentario')
    
    actions = ['aprobar_comentarios']

    def aprobar_comentarios(self,request,query):
        queryset.update(aprobado=True)

admin.site.register(Comentario,ComentariosAdmin)

