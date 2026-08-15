from django import forms
from django.utils import timezone

from .models import Booking, Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["student_id", "course", "year_of_study", "bio"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["student_name", "date", "start_time", "end_time"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, space=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.space = space
        # whole hour chunks.
        first = space.opening_time.hour if space else 0
        last = space.closing_time.hour if space else 23
        hours = [f"{h:02d}:00" for h in range(first, last + 1)]
        self.fields["start_time"].widget = forms.Select(
            choices=[(h, h) for h in hours[:-1]]
        )
        self.fields["end_time"].widget = forms.Select(
            choices=[(h, h) for h in hours[1:]]
        )

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get("start_time")
        end = cleaned.get("end_time")
        date = cleaned.get("date")
        if not (start and end and date):
            return cleaned
        if start >= end:
            raise forms.ValidationError("End time must be after start time.")
        now = timezone.localtime()
        if date < now.date() or (date == now.date() and start < now.time()):
            raise forms.ValidationError("You can't book a time in the past.")
        if self.space:
            if start < self.space.opening_time or end > self.space.closing_time:
                raise forms.ValidationError(
                    f"This space is open {self.space.opening_time:%H:%M}"
                    f"-{self.space.closing_time:%H:%M}."
                )
            overlap = self.space.bookings.filter(
                date=date, start_time__lt=end, end_time__gt=start
            ).exists()
            if overlap:
                raise forms.ValidationError(
                    "This space is already booked during that time."
                )
        return cleaned


class SpaceSearchForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hour = forms.TypedChoiceField(
        coerce=int,
        choices=[(h, f"{h:02d}:00-{h + 1:02d}:00") for h in range(24)],
        label="Time slot",
    )


class WellbeingContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your name")
    message = forms.CharField(widget=forms.Textarea, label="Your message")
