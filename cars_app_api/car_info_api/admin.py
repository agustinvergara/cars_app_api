
from django.contrib import admin
import django.apps


#aca usamos un modulo que esta build in en django el cual nos permite fetchear los modelos de models.py y los mnete en una lista (por verificar)
models = django.apps.apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass