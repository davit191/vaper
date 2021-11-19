from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("article/<int:news_id>/", views.newser, name="newser"),
    path("news/", views.ollnews, name="ollnews"),
    path("contacts/", views.contakt, name="contacts"),
    path("<slug:slug>", views.getCategory, name="getCategory"),
]
