from django.db import models
from ckeditor.fields import RichTextField, RichTextFormField
class Post(models.Model):

    title = models.CharField(max_length=200,default='unnamed title',null=False)
    slug = models.SlugField(max_length=200)
    pub_date = models.DateTimeField('date published')
    intro = models.TextField(max_length=200)
    body = RichTextField()

    def __str__(self):
        return self.title
class Tag(models.Model):

    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    count = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, null=True,blank=True)
    nice_name = models.CharField(max_length=20)
    email = models.EmailField(null=True,blank=True)
    content = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    
    def __str__(self):
        return self.nice_name