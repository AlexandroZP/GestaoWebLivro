from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Livro
from django.shortcuts import redirect


def home(request):
    livros = Livro.objects.all()
    status = request.GET.get('status')
    return render(request, 'home.html', {'livros':livros, 'status':status})


def detalhar_livro(request, id):
    livro = Livro.objects.get(id = id)
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


def deletar_livro(request, come_from, id):
    livro = Livro.objects.get(id = id)
    if come_from == 1:
        return render(request, 'deletar_livro.html', {'livro':livro})
    elif come_from == 2:
        livro.delete()
        return redirect('/livros/home/?status=0')
    elif come_from == 3:
        return redirect('/livros/home/')


def editar_livro(request, id):
    livro = Livro.objects.get(id = id)


    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'editar_livro.html', {'status':status, 'livro':livro})
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        finalizado = request.POST.get('finalizado')
        resenha = request.POST.get('resenha')
        
        if len(nome.strip()) == 0 or len(resenha.strip()) == 0:
            return redirect(f'/livros/editar_livro/{livro.id}?status=1', {'livro':livro})
        

        if finalizado == "on":
            finalizado = True
        else:
            finalizado = False


        try:       
            livro.nome = nome
            livro.resenha = resenha
            livro.finalizado = finalizado 
            livro.save()
            return redirect(f'/livros/editar_livro/{livro.id}?status=0')
        except:
            return redirect(f'/livros/editar_livro/{livro.id}?status=2')


        

    




    

        
