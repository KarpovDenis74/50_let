from django.contrib import admin

from apps.core.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("pk",
                    "confirmation_code",
                    "signer_password",
                    "password",
                    "get_password",
                    "username", "first_name", "last_name",
                    "middle_name", "foto", "email", "phone", "t_nick",
                    "is_staff", "is_active", "date_joined")
    search_fields = ("username", "first_name", "last_name", "email")
    list_filter = ("email",)
    empty_value_display = "-пусто-"

    def get_password(self, obj):
        return obj.password_from_hash()

admin.site.register(User, UserAdmin)
