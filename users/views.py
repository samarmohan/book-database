from .form import UserRegisterForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        messages.success(request, f"{username}, your account was created! Please log in.")
        return HttpResponseRedirect("/login")
    return render(request, "register.html", {"form": form})
