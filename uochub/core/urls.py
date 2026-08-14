from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_page, name="login"),
    path("profile/", views.profile, name="profile"),
    path("map/", views.campus_map, name="campus-map"),
    path("study-spaces/", views.study_spaces, name="study-spaces"),
    path("wellbeing/", views.wellbeing, name="wellbeing"),
    path("directory/", views.directory, name="directory"),
    path("calendar/", views.calendar, name="calendar"),
]
