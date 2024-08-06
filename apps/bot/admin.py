from apps.bot.models import Assistant, GroupBot, TypeGPT
from django.contrib import admin


class TypeGPTAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ['name',]
    list_per_page = 10


class AssistantAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'token', 'folder')
    search_fields = ['name',]
    list_per_page = 10


class GroupBotAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'token', 'group_id', 'active',
                    'assistant')
    search_fields = ['name',]
    list_per_page = 10


admin.site.register(Assistant, AssistantAdmin)
admin.site.register(GroupBot, GroupBotAdmin)
admin.site.register(TypeGPT, TypeGPTAdmin)
