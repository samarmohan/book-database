from django.urls import path
from .views import rules_view, license_view

urlpatterns = [
    path("rules/", rules_view, name="rules"),
    path("license/", license_view, name="license")
]