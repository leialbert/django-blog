from django.contrib import admin
from django.db.models import fields
from .models import Post,Tag,Comment

class TagInline(admin.TabularInline):
    model = Tag
    fields = ['name']
class PostAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]
    list_display = ['title','slug','pub_date']
    # date_hierarchy = 'pub_date'
    list_filter = ['pub_date']
    search_fields = ['title']

# class TagAdmin(admin.ModelAdmin):
#     list_display = ['name','count']
#     readonly_fields = ['count']



admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
