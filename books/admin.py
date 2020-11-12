from django.contrib import admin
from .models import BookResponse


class BookResponseAdmin(admin.ModelAdmin):
    list_display = ("Name", "Email", "Title", "Author", "Description", "Rating")


admin.site.register(BookResponse, BookResponseAdmin)
