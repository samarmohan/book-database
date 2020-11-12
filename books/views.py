from django.shortcuts import render, HttpResponseRedirect
from .models import BookResponse
from .forms import BookResponseForm


def add_book_view(request):
    form = BookResponseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, "create.html", {"form": form})


def home_view(request):
    Book_ResponseHome = BookResponse.objects.all()
    return render(request, "home.html", {"BR": Book_ResponseHome})


def update_view(request, title):
    instance = BookResponse.objects.get(Title=title)
    form = BookResponseForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, "update.html", {"form": form})

