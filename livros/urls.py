from django.urls import path
from . import views

urlpatterns = [
    path('detalhar_livro/', views.detalhar_livro, name="detalhar_livro"),
    path('criar_livro/', views.criar_livro, name="criar_livro"),
]