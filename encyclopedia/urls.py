from django.urls import path

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_view, name='entry'),
    path("search", views.search, name='search'),
    path("create", views.create_view, name='create'),
    path("new", views.create_entry, name='new'),
    path("wiki/edit/<str:title>", views.edit_view, name='edit'),
    path("edit", views.edit_entry, name='edit_entry'),
    path("random", views.random, name='random'),
]
