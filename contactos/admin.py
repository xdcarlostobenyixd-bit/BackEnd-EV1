import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Contacto

# Branding del Admin para Caso 3
admin.site.site_header = "Administración de Agenda de Contactos"
admin.site.site_title = "Agenda Admin"
admin.site.index_title = "Gestión de Contactos Personales"

@admin.action(description="Exportar contactos seleccionados a CSV")
def exportar_a_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contactos.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Apellido', 'Email', 'Teléfono', 'Dirección', 'Fecha Registro'])
    for obj in queryset:
        writer.writerow([obj.nombre, obj.apellido, obj.email, obj.telefono, obj.direccion, obj.fecha_creacion])
    return response

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'fecha_creacion')
    search_fields = ('nombre', 'apellido', 'email')  # Exigido en pauta Caso 3
    list_filter = ('fecha_creacion',)
    actions = [exportar_a_csv]  # Acción personalizada