from django.contrib import admin

from .models import Building, StudySpace


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(StudySpace)
class StudySpaceAdmin(admin.ModelAdmin):
    list_display = ("name", "building", "slug")
    prepopulated_fields = {"slug": ("name",)}
