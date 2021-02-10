from .models import BookModel
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filters import BookFilter


class BookListView(ListView):
    model = BookModel
    context_object_name = "books"
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context


class BookCreateView(CreateView, LoginRequiredMixin):
    model = BookModel
    template_name = "create.html"
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


class BookUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    model = BookModel
    context_object_name = 'book'
    template_name = "update.html"
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
        if self.request.user == book.author:
            return True
        return False


class BookDetailView(DetailView, LoginRequiredMixin):
    model = BookModel
    context_object_name = 'book'
    template_name = "detail.html"
    slug_field = "Title"
    slug_url_kwarg = "Title"

