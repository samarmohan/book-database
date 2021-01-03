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
from books.api import CreateAPI, ListAPI, RetrieveAPI, UpdateAPI, DeleteAPI
from frontend.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-book/', add_book_view),
    path('<title>/update/', update_view),
    path('<title>/detail/', detail_view),
    path('api/books/create/', CreateAPI.as_view()),
    path('api/books/', ListAPI.as_view()),
    path('api/books/<Title>/detail/', RetrieveAPI.as_view()),
    path('api/books/<Title>/update/', UpdateAPI.as_view()),
    path('api/books/<Title>/delete/', DeleteAPI.as_view()),
    path('', home_view),
    path('dev/', index)
]

urlpatterns += staticfiles_urlpatterns()
