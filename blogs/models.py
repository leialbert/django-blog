from django.db import models
from django.db.models.fields import CharField, DateTimeField, EmailField, TextField

class Post(models.Model):
    def __str__(self) -> str:
        return super().__str__()
    title = CharField(max_length=200,null=False)
    pub_date = DateTimeField('date published')
    content = TextField(max_length=10000)


class Tag(models.Model):
    def __str__(self) -> str:
        return super().__str__()
    tag_name = CharField(max_length=20)

class Comment(models.Model):
    def __str__(self) -> str:
        return super().__str__()
    nice_name = CharField(max_length=20)
    email = EmailField()
    comment = CharField(max_length=400)
