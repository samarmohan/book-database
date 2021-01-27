from django.contrib import admin
from .models import BookModel


class BookAdmin(admin.ModelAdmin):
    list_display = ("Name", "Email", "Title", "Author", "PageCount")


admin.site.register(BookModel, BookAdmin)
