from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import WellbeingContactForm
from .models import Building


def home(request):
    return render(request, "core/home.html", {"title": "Home"})


def profile(request):
    return render(request, "core/page.html", {"title": "Profile", "icon": "icons/profile.svg"})


def campus_map(request):
    return render(request, "core/page.html", {"title": "Campus Map", "icon": "icons/campus-map.svg"})


def study_spaces(request):
    return render(
        request,
        "core/page.html",
        {"title": "Study Spaces", "icon": "icons/study-spaces.svg", "show_back": True},
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
