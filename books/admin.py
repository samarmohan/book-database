from django.contrib import admin
from .models import BookModel


# Display custom fields in admin panel
class BookAdmin(admin.ModelAdmin):
    list_display = ("Name", "Email", "Title", "Author", "PageCount")


admin.site.register(BookModel, BookAdmin)
