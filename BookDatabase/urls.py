from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("books.urls")),
    path('', include("users.urls")),
    path('', include("pages.urls")),
    path('api/books/', include("books.api-urls")),
]

urlpatterns += staticfiles_urlpatterns()
