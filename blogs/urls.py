from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('home/', views.home),
    path('posts/',views.list, name='list'),
    path('posts/<slug:slug>/',views.post, name='post'),
    path('about/',views.about, name='about'),
    path('tags/',views.cloudtag, name='cloudtag'),
    path('tags/<str:tagname>/',views.tagdetail, name='tagdetail'),
]