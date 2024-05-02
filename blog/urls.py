from django.urls import path
from . import views
urlpatterns = [
    path('blogs', views.blogs, name='blogs'),
    path('blog/<int:blog_id>', views.blog, name= 'blog'),
    path('blog_search', views.blog_search, name ='blog_search')
]
