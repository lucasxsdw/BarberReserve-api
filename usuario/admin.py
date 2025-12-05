from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Campos extras na edição de usuário
    fieldsets = UserAdmin.fieldsets + (
        ("Dados adicionais", {
            "fields": (
                "telefone",
                "tipo_perfil",
            ),
        }),
    )

    # Campos extras ao criar usuário
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Dados adicionais", {
            "fields": (
                "telefone",
                "tipo_perfil",
            ),
        }),
    )

    list_display = (
        "username",
        "email",
        "first_name",
        "telefone",
        "tipo_perfil",
        "is_staff",
    )
