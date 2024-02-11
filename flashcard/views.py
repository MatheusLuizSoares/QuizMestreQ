from django.shortcuts import render,redirect
from .models import Categoria,Flashcard
from django.http import response
from django.contrib.messages import constants
from django.contrib import messages
def novo_flashcard(request):
  if not request.user.is_authenticated:
    return redirect('/usuarios/logar')
  
  if request.method=="GET":
    categorias=Categoria.objects.all()
    
    dificuldades=Flashcard.DIFICULDADE_CHOICE
    return render (request, "novo_flashcard.html",{'categorias':categorias,"dificuldades":dificuldades})
  elif request.method=="POST":
       pergunta=request.POST.get('pergunta')
       resposta=request.POST.get('resposta')
       categoria=request.POST.get('categoria')
       dificuldade=request.POST.get("dificuldade")
       if len(pergunta.strip())==0 or len(resposta.strip())==0:
         messages.add_message(request,constants.ERROR,"Preenchar os campos de pergunta e resposta")
         redirect("/flashcard/novo_flashcard/")
         
        
