from django.contrib import admin
from django.urls import path, include   # <-- include is imported here

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todo.urls")),
]