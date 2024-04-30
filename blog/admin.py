from django.contrib import admin
from .models import Blogs

@admin.register(Blogs)
class  BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'blog_img', 'date_posted' )