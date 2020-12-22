"""BookDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from books.views import home_view, add_book_view, update_view, detail_view
from books.viewsets import BookResponseCreate, BookResponseGet, BookResponseRetrieveSingle, BookResponseUpdate, BookResponseDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-book/', add_book_view),
    path('<title>/edit', update_view),
    path('<title>/view', detail_view),
    path('api/books/create', BookResponseCreate.as_view()),
    path('api/books', BookResponseGet.as_view()),
    path('api/books/<int:pk>/detail', BookResponseRetrieveSingle.as_view()),
    path('api/books/<int:pk>/update', BookResponseUpdate.as_view()),
    path('api/books/<int:pk>/delete', BookResponseDelete.as_view()),
    path('', home_view)
]

urlpatterns += staticfiles_urlpatterns()
