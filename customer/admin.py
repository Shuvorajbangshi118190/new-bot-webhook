
from django.contrib import admin
from .models import CustomerList




class CustomerListAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url', 'created_at', 'updated_at', 'status', 'code', 'provider')

admin.site.register(CustomerList, CustomerListAdmin)