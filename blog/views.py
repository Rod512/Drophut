from django.shortcuts import render,get_object_or_404
from .models import Blogs,Comment
from django.contrib.auth.models import User

def blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog/blogs.html', {'blogs': blogs})

def blog(request,blog_id):
    if request.method == "POST":
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']

        query = Comment(message = message)
        query.name = name
        query.email = email
        query.save()
    comment = Comment.objects.filter(post_id = blog_id)
    blog = get_object_or_404(Blogs, pk = blog_id)
    blogs = Blogs.objects.all()
    context = {
        'blog': blog,
        'blogs' : blogs,
        'comments' : comment,
    }
    return render(request, 'blog/blog.html',context)


def blog_search(request):
    if request.method == 'POST':
        blog_searched = request.POST['blog_searched']
        blog = Blogs.objects.filter(title__contains = blog_searched)
        return render(request, 'blog/blog.html',{'blog_searched':blog_searched,'blogs':blog}) 
    else:
        return render(request, 'blog/blog.html') 

