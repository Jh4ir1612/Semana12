
from django.contrib import admin
from .models import Autor, Libro

class LibroInline(admin.TabularInline):
    model = Libro
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    inlines = [LibroInline]
    list_display = ('nombre', 'correo')
    search_fields = ('nombre',)

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    list_filter = ('autor', 'fecha_publicacion')
    search_fields = ('titulo',)

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
