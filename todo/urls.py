from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    path(
        "register/",
        views.register,
        name="register"
    ),
    path(
    "add-task/",
    views.add_task,
    name="add_task"
),
    path(
    "edit-task/<int:pk>/",
    views.edit_task,
    name="edit_task"
),

    path(
    "delete-task/<int:pk>/",
    views.delete_task,
    name="delete_task"
),



]