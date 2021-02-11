from .models import BookModel
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filters import BookFilter


class BookListView(ListView):
    model = BookModel
    context_object_name = "books"
    template_name = "books/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context


class BookCreateView(LoginRequiredMixin, CreateView):
    model = BookModel
    template_name = "books/create.html"
    success_url = "/"
    fields = [
        "Title",
        "Author",
        "Description",
        "PageCount",
        "GradeLevel",
        "Rating"
    ]

    def form_valid(self, form):
        form.instance.Name = self.request.user
        form.instance.Email = self.request.user.email

        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BookModel
    context_object_name = 'book'
    template_name = "books/update.html"
    slug_field = "Title"
    slug_url_kwarg = "Title"
    success_url = "/"
    fields = [
            "Title",
            "Author",
            "Description",
            "PageCount",
            "GradeLevel",
            "Rating"
        ]

    def form_valid(self, form):
        form.instance.Name = self.request.user.username
        form.instance.Email = self.request.user.email
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.Name:
            return True
        return False


class BookDetailView(DetailView, LoginRequiredMixin):
    model = BookModel
    context_object_name = 'book'
    template_name = "books/detail.html"
    slug_field = "Title"
    slug_url_kwarg = "Title"

