from django.contrib import admin
from django.apps import apps
from .models import EndUsers


@admin.register(EndUsers)
class EndUsersAdmin(admin.ModelAdmin):
    list_display = ["user", "email", "joined_date"]
    search_fields = ["user", "email"]


models_to_ignore = []

for model in apps.get_models():
    try:
        if model._meta.label in models_to_ignore:
            continue
        else:

            class modelAdmin(admin.ModelAdmin):
                list_display = [field.name for field in model._meta.fields]

            admin.site.register(model, modelAdmin)
    except admin.sites.AlreadyRegistered:
        pass
