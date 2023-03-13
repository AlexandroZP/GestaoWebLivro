from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('detalhar_livro/<int:id>', views.detalhar_livro, name="detalhar_livro"),
    path('criar_livro/', views.criar_livro, name="criar_livro"),
]