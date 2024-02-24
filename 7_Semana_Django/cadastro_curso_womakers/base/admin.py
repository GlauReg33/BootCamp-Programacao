from django.contrib import admin
from base.models import cadastro

# Register your models here.
@admin.register(cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']