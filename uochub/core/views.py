from django.shortcuts import render


def home(request):
    return render(request, "core/home.html", {"title": "Home"})


def profile(request):
    return render(request, "core/page.html", {"title": "Profile"})


def campus_map(request):
    return render(request, "core/page.html", {"title": "Campus Map"})


def study_spaces(request):
    return render(request, "core/page.html", {"title": "Study Spaces"})


def wellbeing(request):
    return render(request, "core/page.html", {"title": "Wellbeing"})


def directory(request):
    return render(request, "core/page.html", {"title": "Campus Directory"})


def calendar(request):
    return render(request, "core/page.html", {"title": "Academic Calendar"})
