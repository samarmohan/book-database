from django.shortcuts import render


def rules_view(request):
    return render(request, "rules.html")


def license_view(request):
    return render(request, "license.html")