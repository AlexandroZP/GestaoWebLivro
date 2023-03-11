from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro
from django.shortcuts import redirect
# Create your views here.
def detalhar_livro(request):
    livro = Livro.objects.filter(id=1)
    print(livro)
    return render(request, 'detalhar_livro.html', {'nome':livro[0].nome,'finalizado':livro[0].finalizado, 'resenha':livro[0].resenha})


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



        
