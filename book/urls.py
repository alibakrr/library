from django.contrib import admin
from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_book/', views.add_book, name="add_book"),
    path('update/<int:id>', views.updateBook, name="update"),
    path('book/<int:id>', views.detail, name="detail"),
    path('delete/<int:id>', views.deleteBook, name="delete"),
    path('', views.books, name="books"),
    path('comment/<int:id>', views.comment, name="comment"),

]