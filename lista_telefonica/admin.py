from django.contrib import admin
from  lista_telefonica.models import Contato
from lista_telefonica.models import Anuncio
# Register your models here.

admin.site.register(Contato)
admin.site.register(Anuncio)