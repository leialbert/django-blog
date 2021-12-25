from django.contrib import admin
from .models import Post,Tag,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','pub_date']

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
