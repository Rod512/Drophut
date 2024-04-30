from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Blogs

def blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def paginator(request):
    blogs = Blogs.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(blogs, 2)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'blogs': paged_listings,
    }
    return render(request, 'blog/blogs.html', context)

