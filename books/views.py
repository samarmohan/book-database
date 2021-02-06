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
    title_contains_query = request.GET.get("title")
    author_contains_query = request.GET.get("author")
    name_contains_query = request.GET.get("name")
    rating_contains_query = request.GET.get("rating")

    if title_contains_query != "" and title_contains_query is not None:
        book_response_home_list = book_response_home_list.filter(Title__icontains=title_contains_query)

    elif author_contains_query != "" and author_contains_query is not None:
        book_response_home_list = book_response_home_list.filter(Author__icontains=author_contains_query)

    elif name_contains_query != "" and name_contains_query is not None:
        book_response_home_list = book_response_home_list.filter(Name__icontains=name_contains_query)

    elif rating_contains_query != "" and rating_contains_query is not None:
        book_response_home_list = book_response_home_list.filter(Rating__icontains=rating_contains_query)

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
