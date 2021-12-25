from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.utils import timezone

from blogs.models import Post,Tag

context = {
        'BASE_URL':settings.BASE_URL,
        'SITE_NAME':settings.SITE_NAME,
        'SUBTITLE':settings.SUBTITLE,
        # 'THEME_NAME':settings.THEME_NAME,
        'NAVS':settings.NAVS,
        'AVATAR':settings.AVATAR,
        'COPYRIGHT':settings.COPYRIGHT,
        'SOCIAL':settings.SOCIAL,
        'GOOGLE_ANALYTICS_ID':settings.GOOGLE_ANALYTICS_ID,
    }


def home(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:1]
    context['posts'] = posts
    return render(request, 'blogs/home.html',context)
def list(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:4]
    context['posts'] = posts
    return render(request, 'blogs/list.html',context)

def post(request,id):
    post = Post.objects.get(pk=id)
    tags = Tag.objects.filter(post__id=id)
    context['tags'] = tags
    context['post'] = post
    return render(request, 'blogs/post.html',context)

def about(request):
    return render(request, 'blogs/about.html',context)

def cloudtag(request):
    tags = Tag.objects.all()
    context['tags'] = tags
    return render(request, 'blogs/tags.html',context)

def tagdetail(request, tagname):
    return render(request, 'blogs/tagdetail.html',context)