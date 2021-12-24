from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title':'Hello Blog',
    }
    return render(request, 'blogs/index.html',context)
