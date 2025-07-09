from django.contrib import admin
from .models import Integrante, Guardia

@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'activo', 'fecha_creacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['nombre', 'apellido']
    ordering = ['apellido', 'nombre']

@admin.register(Guardia)
class GuardiaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'fecha', 'total_integrantes', 'activa', 'fecha_creacion']
    list_filter = ['activa', 'fecha', 'numero', 'fecha_creacion']
    search_fields = ['numero']
    date_hierarchy = 'fecha'
    filter_horizontal = ['integrantes']
    
    def total_integrantes(self, obj):
        return obj.total_integrantes
    total_integrantes.short_description = 'Total Integrantes'
