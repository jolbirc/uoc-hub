from django.shortcuts import render


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
    return render(
        request,
        "core/page.html",
        {"title": "Wellbeing", "icon": "icons/wellbeing-icon.svg", "show_back": True},
    )


def directory(request):
    return render(
        request,
        "core/page.html",
        {"title": "Campus Directory", "icon": "icons/campus-directory.svg", "show_back": True},
    )


def calendar(request):
    return render(
        request,
        "core/page.html",
        {"title": "Academic Calendar", "icon": "icons/academic-calendar.svg", "show_back": True},
    )
