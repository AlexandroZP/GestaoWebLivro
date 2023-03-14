from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Livro
from django.shortcuts import redirect


def home(request):
    livros = Livro.objects.all()
    return render(request, 'home.html', {'livros':livros})


def detalhar_livro(request,id):
    livro = Livro.objects.get(id = id)
    print(livro)
    return render(request, 'detalhar_livro.html', {'livro':livro})


def criar_livro(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'criar_livro.html',{'status':status})
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        finalizado = request.POST.get('finalizado')
        resenha = request.POST.get('resenha')

        if finalizado == "on":
            finalizado = True
        else:
            finalizado = False
        
        livro = Livro.objects.filter(nome = nome)

        if len(nome.strip()) == 0 or len(resenha.strip()) == 0:
            return redirect('/livros/criar_livro/?status=1')

        if len(livro) > 0:
            return redirect('/livros/criar_livro/?status=2')
        
        try:       
            livro = Livro(nome = nome, finalizado = finalizado, resenha=resenha)
            livro.save()
            return redirect('/livros/criar_livro/?status=0')
        
        except:
            return redirect('/livros/criar_livro/?status=3')


def deletar_livro(request, id):
    livro = Livro.objects.get(id = id)
    n_livro = livro.nome
    livro.delete()
    return render(request, 'deletar_livro.html', {'n_livro':n_livro})




    

        
