import datetime

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingForm, SpaceSearchForm, WellbeingContactForm
from .models import Building, StudySpace


def home(request):
    return render(request, "core/home.html", {"title": "Home"})


def profile(request):
    return render(request, "core/page.html", {"title": "Profile", "icon": "icons/profile.svg"})


def campus_map(request):
    return render(request, "core/page.html", {"title": "Campus Map", "icon": "icons/campus-map.svg"})


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


def directory(request):
    buildings = Building.objects.all()
    return render(
        request,
        "core/directory.html",
        {"title": "Campus Directory", "buildings": buildings},
    )


def calendar(request):
    return render(
        request,
        "core/page.html",
        {"title": "Academic Calendar", "icon": "icons/academic-calendar.svg", "show_back": True},
    )
