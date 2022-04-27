from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import  *



@admin.register(Ustoz)
class UstozAdmin(ModelAdmin):
    search_fields = ('id','ism')
    list_filter = ('nafaqada',)
@admin.register(Fan)
class FanAdmin(ModelAdmin):
    search_fields = ('id', 'nom',)
    autocomplete_fields = ('yonalish',)


