from django.http.response import HttpResponse
from django.shortcuts import render

from blogs.models import Tag

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
    tags = Tag.objects.all()
    context = {
        'tags':tags,
    }
    return render(request, 'blogs/tags.html',context)

def tagdetail(request, tagname):
    return render(request, 'blogs/tagdetail.html')