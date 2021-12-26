from os import name
from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [ 
    path('', views.home, name='home'),
    path('home/', views.home),
    path('posts/',views.list, name='list'),
    path('posts/<int:id>/',views.post, name='post'),
    path('about/',views.about, name='about'),
    path('tags/',views.cloudtag, name='cloudtag'),
    path('tags/<str:tagname>/',views.tagdetail, name='tagdetail'),
    path('page/<int:id>/',views.page, name='page'),
]