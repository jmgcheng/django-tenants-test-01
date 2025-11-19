from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("", include("public.urls")),  # landing + pricing
    path("admin/", admin.site.urls),
]
