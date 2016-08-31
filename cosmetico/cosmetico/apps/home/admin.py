from django.contrib import admin
from cosmetico.apps.home.models import *

admin.site.register(Marca)
admin.site.register(Cosmetico)
admin.site.register(Categoria)
admin.site.register(Color)
admin.site.register(Ingredientes)
admin.site.register(Advertencias)

admin.site.register(user_profile)