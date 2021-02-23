from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from .filters import BookFilter
from .models import BookModel


# Home page view
class BookListView(ListView):
    model = BookModel
    context_object_name = "books"
    template_name = "books/home.html"

    # Filtering function
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context


# Create page view
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

    # Set Name and Email to the logged in username and email
    def form_valid(self, form):
        form.instance.Name = self.request.user.first_name + "  " + self.request.user.last_name
        form.instance.Email = self.request.user.email

        return super().form_valid(form)


# Update page view
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

    # Set Name and Email to the logged in username and email
    def form_valid(self, form):
        form.instance.Name = self.request.user.first_name + "  " + self.request.user.last_name
        form.instance.Email = self.request.user.email
        return super().form_valid(form)

    # Makes sure the person trying to edit is the one that actually created the book.
    def test_func(self):
        book = self.get_object()
        if self.request.user.first_name + "  " + self.request.user.last_name == book.Name and self.request.user.email == book.Email:
            return True
        return False


# Detail page view
class BookDetailView(DetailView, LoginRequiredMixin):
    model = BookModel
    context_object_name = 'book'
    template_name = "books/detail.html"
    slug_field = "Title"
    slug_url_kwarg = "Title"
