from django.shortcuts import render, HttpResponseRedirect
from .models import BookModel
from .forms import BookForm


def add_book_view(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, "create.html", {"form": form})


def home_view(request):
    book_response_home_list = BookModel.objects.all()
    return render(request, "home.html", {"books": book_response_home_list})


def update_view(request, title):
    instance = BookModel.objects.get(Title=title)
    form = BookForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, "update.html", {"form": form})


def detail_view(request, title):
    book_response_detail = BookModel.objects.get(Title=title)
    return render(request, "detail.html", {"book": book_response_detail})
