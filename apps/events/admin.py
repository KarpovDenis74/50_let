from django.contrib import admin

from apps.events.models import Event, SamplePeriod, EventGuest


class EventGuestInline(admin.TabularInline):
    model = EventGuest
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = (EventGuestInline,)
    list_display = ("pk", "name", "description", "place",
                    "start", "stop", "created_at", "created_at")
    search_fields = ("name", "description")
    list_filter = ("start", "stop")
    empty_value_display = "-пусто-"


class SamplePeriodAdmin(admin.ModelAdmin):
    list_display = ("pk", "event", "start", "stop")
    search_fields = ("event__name", "start", "stop")
    empty_value_display = "-пусто-"


admin.site.register(Event, EventAdmin)
admin.site.register(SamplePeriod, SamplePeriodAdmin)
