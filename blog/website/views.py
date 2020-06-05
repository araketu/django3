from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_blog(request):
    data = {'name':' Curso Django3'}
    # return HttpResponse('Blog')
    return render (request, 'index.html',data)