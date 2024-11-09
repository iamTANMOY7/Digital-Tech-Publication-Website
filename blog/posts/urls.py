from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("search", views.search, name="search"),
    path("description/<int:id>/", views.description, name="description"),
    path("demo", views.demo, name="demo"),
]
