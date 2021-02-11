from django.shortcuts import render


def rules_view(request):
    return render(request, "pages/rules.html")


def license_view(request):
    return render(request, "pages/license.html")