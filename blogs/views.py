from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.utils import timezone
from django.core.paginator import Paginator

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
        'PAGINATE':settings.PAGINATE,
    }


def home(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    paginator = Paginator(posts,settings.PAGINATE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'blogs/home.html',context)
def list(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    paginator = Paginator(posts,settings.PAGINATE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'blogs/list.html',context)

def page(request,id):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    paginator = Paginator(posts,settings.PAGINATE)
    page_number = id
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'blogs/page.html',context)

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
    for i in tags:
        i.count = Post.objects.filter(tag__name=i.name).count()
    return render(request, 'blogs/tags.html',context)

def tagdetail(request, tagname):
    posts = Post.objects.filter(tag__name=tagname)
    context['posts'] = posts
    context['tagname'] = tagname
    return render(request, 'blogs/tagdetail.html',context)