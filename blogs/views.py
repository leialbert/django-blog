from django.http.response import HttpResponse
from django.shortcuts import render

def home(request):
    context = {
        'title':'Hello Blog',
    }
    return render(request, 'blogs/home.html',context)
def list(request):
    return render(request, 'blogs/list.html')

def post(request,slug):

    return render(request, 'blogs/post.html')

def about(request):
    return render(request, 'blogs/about.html')

def cloudtag(request):
    return render(request, 'blogs/tags.html')

def tagdetail(request, tagname):
    return render(request, 'blogs/tagdetail.html')