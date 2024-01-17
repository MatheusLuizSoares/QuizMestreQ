from django.shortcuts import render,redirect
from django.http import HttpResponse
def cadastro(request):
  if request.method=="GET":
    return render(request,"cadastro.html")
  elif request.method=="POST":
    return 