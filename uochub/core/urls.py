from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="core/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("map/", views.campus_map, name="campus-map"),
    path("study-spaces/", views.study_spaces, name="study-spaces"),
    path("wellbeing/", views.wellbeing, name="wellbeing"),
    path("directory/", views.directory, name="directory"),
    path("calendar/", views.calendar, name="calendar"),
]
