from django.contrib import admin

from .models import Booking, Building, StudySpace


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(StudySpace)
class StudySpaceAdmin(admin.ModelAdmin):
    list_display = ("name", "building", "slug", "opening_time", "closing_time")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("space", "student_name", "date", "start_time", "end_time")
    list_filter = ("space", "date")
