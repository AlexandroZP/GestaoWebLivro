from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('detalhar_livro/<int:id>', views.detalhar_livro, name="detalhar_livro"),
    path('criar_livro/', views.criar_livro, name="criar_livro"),
    path('deletar_livro/<int:id>/<int:come_from>', views.deletar_livro, name="deletar_livro"),
    path('editar_livro/<int:id>', views.editar_livro, name="editar_livro"),
]