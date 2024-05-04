from django.contrib import admin
from .models import Blogs,Comment

@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'blog_img', 'date_posted' )

@admin.register(Comment)
class CommentAmdin(admin.ModelAdmin):
    list_display = ('name','email','message')