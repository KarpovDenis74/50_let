from django.contrib import admin

from apps.core.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "username", "first_name", "last_name",
                    "middle_name", "foto", "email", "phone", "t_nick")
    search_fields = ("username", "first_name", "last_name", "email")
    list_filter = ("email",)
    empty_value_display = "-пусто-"


admin.site.register(User, UserAdmin)
