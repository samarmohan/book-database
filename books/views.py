from django.shortcuts import render, HttpResponseRedirect
from .models import BookModel
from .forms import BookForm
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home_view(request):
    book_response_home_list = BookModel.objects.order_by("-Rating")
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


class BookCreateView(CreateView, LoginRequiredMixin):
    model = BookModel
    fields = [
            "Title",
            "Author",
            "Description",
            "PageCount",
            "GradeLevel",
            "Rating"
        ]
    template_name = "create.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.Name = self.request.user
        form.instance.Email = self.request.user.email

        return super().form_valid(form)


class BookUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    context_object_name = 'book'
    model = BookModel
    fields = [
            "Title",
            "Author",
            "Description",
            "PageCount",
            "GradeLevel",
            "Rating"
        ]
    template_name = "update.html"
    slug_field = "Title"
    slug_url_kwarg = "Title"

    def form_valid(self, form):
        form.instance.Name = self.request.user
        form.instance.Email = self.request.user.email
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.author:
            return True
        return False


class BookDetailView(DetailView, LoginRequiredMixin):
    template_name = "detail.html"
    model = BookModel
    slug_field = "Title"
    slug_url_kwarg = "Title"
    context_object_name = 'book'

