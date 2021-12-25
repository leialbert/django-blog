from django.db import models

from djangoblog.settings import TIME_ZONE
class Post(models.Model):

    title = models.CharField(max_length=200,default='unnamed title',null=False)
    slug = models.SlugField(max_length=200)
    pub_date = models.DateTimeField('date published')
    intro = models.TextField(max_length=200)
    body = models.TextField(max_length=10000)

    def __str__(self):
        return self.title
class Tag(models.Model):

    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, null=True,blank=True)
    nice_name = models.CharField(max_length=20)
    email = models.EmailField()
    content = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    
    def __str__(self):
        return self.nice_name