import datetime

from django.db import models
from django.utils import timezone


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
    opening_time = models.TimeField(default=datetime.time(9))
    closing_time = models.TimeField(default=datetime.time(17))

    def __str__(self):
        return self.name

    def availability_now(self):
        now = timezone.localtime()
        if not (self.opening_time <= now.time() < self.closing_time):
            return "closed"
        booked = self.bookings.filter(
            date=now.date(), start_time__lte=now.time(), end_time__gt=now.time()
        ).exists()
        return "in use" if booked else "free"


class Booking(models.Model):
    space = models.ForeignKey(
        StudySpace, on_delete=models.CASCADE, related_name="bookings"
    )
    student_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.space} on {self.date} {self.start_time}-{self.end_time}"
