from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings

from blogs.models import Tag

base_url = settings.BASE_URL
navs = settings.NAVS


def home(request):
    context = {
        'BASE_URL':base_url,
        'NAVS':navs,
    }
    return render(request, 'blogs/home.html',context)
def list(request):
    context = {
        'BASE_URL':base_url,
        'NAVS':navs,
    }
    return render(request, 'blogs/list.html',context)

def post(request,slug):
    context = {
        'BASE_URL':base_url,
        'NAVS':navs,
    }
    return render(request, 'blogs/post.html',context)

def about(request):
    context = {
        'BASE_URL':base_url,
        'NAVS':navs,
    }
    return render(request, 'blogs/about.html',context)

def cloudtag(request):
    tags = Tag.objects.all()
    context = {
        'tags':tags,
        'BASE_URL':base_url,
        'NAVS':navs,
    }
    return render(request, 'blogs/tags.html',context)

def tagdetail(request, tagname):
    context = {
        'BASE_URL':base_url,
        'NAVS':navs,
    }
    return render(request, 'blogs/tagdetail.html',context)