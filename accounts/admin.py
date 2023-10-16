from django.contrib import admin
from .models import CustomUser


class CustomUserListAdmin(admin.ModelAdmin):
    list_display = ('email','first_name', 'last_name')




# Register your models here.
admin.site.register(CustomUser,CustomUserListAdmin)

