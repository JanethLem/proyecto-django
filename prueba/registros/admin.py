from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera','turno', 'created', 'nombreMayus')#ADD 'nombre' on list_display
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')
    #para la paginación
    list_per_page=1

    #Desplegar opciones avanzadas
    fieldsets = (
        (None, {
            'fields' : ('nombre',)
        }),
        ('Opciones avanzadas', {
            'classes' : ('collapse', 'wide', 'extrapretty'),
            'fields': ('matricula', 'carrera', 'turno', 'created')
        })
    )

    #Columna personalizada
    def nombreMayus (self, obj):
        return obj.nombre.upper()

    #Cambiar nombre de la columna sin migrar
    nombreMayus.short_description='Nombre'


    def get_readonly_fields(self, request, obj=None):
        if  request.user.group.filter(name="Usuarios").exists():
            return ('matricula', 'carrera', 'turno')
        else:
            return ('created', 'updated')
    #ordenar de A-Z y para cambiar el orden se pone un -
    #ordering=('nombre',)
    #permite editar los campos desde la vista de alumnos
    #list_editable=('nombre',)
    #permite cambiar el link que dirige al formulario 
    #list_display_links=('nombre',)
    #permite editar en el formulario el dato deseado  
    #exclude=('carrera', 'turno')

admin.site.register(Alumnos, AdministrarModelo)


class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    list_filter = ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    list_filter = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
