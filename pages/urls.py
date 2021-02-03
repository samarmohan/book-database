from django.urls import path
from .views import rules_view, license_view

urlpatterns = [
    path("rules/", rules_view),
    path("license/", license_view)
]