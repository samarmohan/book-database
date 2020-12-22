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
    book_response_home_list = BookResponse.objects.all()
    return render(request, "home.html", {"BR": book_response_home_list})


def update_view(request, title):
    instance = BookResponse.objects.get(Title=title)
    form = BookResponseForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, "update.html", {"form": form})


def detail_view(request, title):
    book_response_detail = BookResponse.objects.get(Title=title)
    return render(request, "detail.html", {"BR": book_response_detail})
