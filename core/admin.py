from django.contrib import admin
from core.models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')  # Na listagem de eventos no adm do site, isso aparecerá
    list_filter = ('titulo', 'usuario', 'data_evento')  # Filtro de pesquisa no admin da listagem de eventos


admin.site.register(Evento, EventoAdmin)
