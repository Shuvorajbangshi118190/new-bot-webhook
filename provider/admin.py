# customer/admin.py
from django.contrib import admin
from .models import ProviderList



class ProviderListAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url', 'created_at', 'updated_at', 'status', 'code')

admin.site.register(ProviderList, ProviderListAdmin)