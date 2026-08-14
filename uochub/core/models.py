from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class StudySpace(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="study_spaces"
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
