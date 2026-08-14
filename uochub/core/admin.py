from django.contrib import admin

from .models import Booking, Building, CalendarEvent, StudySpace


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(StudySpace)
class StudySpaceAdmin(admin.ModelAdmin):
    list_display = ("name", "building", "slug", "opening_time", "closing_time")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    list_filter = ("date",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("space", "student_name", "date", "start_time", "end_time")
    list_filter = ("space", "date")
