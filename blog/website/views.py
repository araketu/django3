from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello_blog(request):
    lista = {'Django','Python',"git",'html', 'Banco de dados'}
    data ={'name': "Curso Django3", 'listatec':lista}
    return render(request, "index.html",data)