import datetime
from calendar import HTMLCalendar

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.html import escape
from django.utils.safestring import mark_safe

from .forms import BookingForm, ProfileForm, SpaceSearchForm, WellbeingContactForm
from .models import Building, CalendarEvent, Profile, StudySpace


@login_required
def home(request):
    return render(request, "core/home.html", {"title": "Home"})


@login_required
def profile(request):
    user_profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=user_profile)
    return render(
        request,
        "core/profile.html",
        {
            "title": "Profile",
            "icon": "icons/profile.svg",
            "profile": user_profile,
            "form": form,
            "editing": request.GET.get("edit") == "1",
        },
    )


@login_required
def campus_map(request):
    buildings = [
        {
            "name": b.name,
            "description": b.description,
            "lat": b.latitude,
            "lng": b.longitude,
        }
        for b in Building.objects.exclude(latitude=None).exclude(longitude=None)
    ]
    return render(
        request,
        "core/campus_map.html",
        {
            "title": "Campus Map",
            "icon": "icons/campus-map.svg",
            "buildings": buildings,
        },
    )


@login_required
def study_spaces(request):
    spaces = StudySpace.objects.select_related("building").all()
    search_form = SpaceSearchForm(request.GET or None)
    searched = False
    if search_form.is_valid():
        searched = True
        date = search_form.cleaned_data["date"]
        hour = search_form.cleaned_data["hour"]
        start = datetime.time(hour)
        end = datetime.time(hour + 1) if hour < 23 else datetime.time.max
        spaces = spaces.filter(
            opening_time__lte=start, closing_time__gte=end
        ).exclude(
            bookings__date=date,
            bookings__start_time__lt=end,
            bookings__end_time__gt=start,
        )
    return render(
        request,
        "core/study_spaces.html",
        {
            "title": "Study Spaces",
            "spaces": spaces,
            "search_form": search_form,
            "searched": searched,
        },
    )


@login_required
def book_space(request, slug):
    space = get_object_or_404(StudySpace, slug=slug)
    if request.method == "POST":
        form = BookingForm(request.POST, space=space)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.space = space
            booking.save()
            return redirect("study-spaces")
    else:
        form = BookingForm(space=space)
    return render(
        request,
        "core/book_space.html",
        {"title": f"Book {space.name}", "space": space, "form": form},
    )


def wellbeing(request):
    if request.method == "POST":
        form = WellbeingContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Wellbeing message from {form.cleaned_data['name']}",
                message=form.cleaned_data["message"],
                from_email="noreply@uochub.example.com",
                recipient_list=["wellbeing@uochub.example.com"],
            )
            return redirect("wellbeing-sent")
    else:
        form = WellbeingContactForm()
    return render(
        request,
        "core/wellbeing.html",
        {
            "title": "Wellbeing",
            "icon": "icons/wellbeing-icon.svg",
            "show_back": True,
            "form": form,
        },
    )


def wellbeing_sent(request):
    return render(
        request,
        "core/wellbeing.html",
        {
            "title": "Wellbeing",
            "icon": "icons/wellbeing-icon.svg",
            "show_back": True,
            "sent": True,
        },
    )


@login_required
def directory(request):
    buildings = Building.objects.all()
    return render(
        request,
        "core/directory.html",
        {"title": "Campus Directory", "buildings": buildings},
    )


class EventCalendar(HTMLCalendar):
    def __init__(self, events):
        super().__init__()
        self.events_by_day = {}
        for event in events:
            self.events_by_day.setdefault(event.date.day, []).append(event)

    def formatday(self, day, weekday):
        if day == 0 or day not in self.events_by_day:
            return super().formatday(day, weekday)
        items = "".join(
            f"<li>{escape(e.title)}</li>" for e in self.events_by_day[day]
        )
        return (
            f'<td class="{self.cssclasses[weekday]}">{day}<ul>{items}</ul></td>'
        )


@login_required
def calendar(request):
    today = timezone.localdate()
    try:
        first = datetime.date(
            int(request.GET.get("year", today.year)),
            int(request.GET.get("month", today.month)),
            1,
        )
    except ValueError:
        first = today.replace(day=1)

    events = CalendarEvent.objects.filter(
        date__year=first.year, date__month=first.month
    )
    month_html = EventCalendar(events).formatmonth(first.year, first.month)
    return render(
        request,
        "core/calendar.html",
        {
            "title": "Academic Calendar",
            "calendar": mark_safe(month_html),
            "prev_month": first - datetime.timedelta(days=1),
            "next_month": (first + datetime.timedelta(days=31)).replace(day=1),
        },
    )
