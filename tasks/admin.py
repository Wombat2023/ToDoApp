from django.contrib import admin
from .models import Aufgabe

@admin.register(Aufgabe)
class AufgabeAdmin(admin.ModelAdmin):
    list_display = ('titel', 'erledigt', 'erstellt_am')
    list_filter = ('erledigt','erstellt_am')
    search_fields = ('titel', 'beschreibung')
    