from django.shortcuts import render,get_object_or_404
from .models import Blogs

def blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog/blogs.html', {'blogs': blogs})

def blog(request,blog_id):
    blog = get_object_or_404(Blogs, pk = blog_id)
    blogs = Blogs.objects.all()
    context = {
        'blog': blog,
        'blogs' : blogs
    }
    return render(request, 'blog/blog.html',context)



