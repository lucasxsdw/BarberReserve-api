from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Dados adicionais", {"fields": ("telefone",)}),
    )
    list_display = ("username", "email", "first_name", "telefone", "is_staff")
