from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("", include("dashboard.urls")),   # tenant dashboard
    path("admin/", admin.site.urls),
]
