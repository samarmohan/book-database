from django.contrib import admin
from .models import BookResponse


class BookResponseAdmin(admin.ModelAdmin):
    list_display = ("Name", "Email", "Title", "Author", "PageCount")


admin.site.register(BookResponse, BookResponseAdmin)
