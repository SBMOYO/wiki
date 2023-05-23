from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("new page/", views.new_page, name="new_page"),
    path("edit_page/", views.edit_page, name="edit_page"),
    path("save_edit", views.save_edit, name="save_edit"),
    path("random_page", views.random_page, name="random_page"),
    path("<str:title>", views.get_title, name="get_title") 
]
