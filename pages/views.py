from django.shortcuts import render
from .models import Products_listing

def home(request):
    products = Products_listing.objects.all()
    return render(request, 'pages/index.html',{'products':products})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Products_listing.objects.filter(product_name__contains =searched)
        return render(request, 'pages/index.html',{'searched':searched, 'products':products})
    
    else:
        return render(request, 'pages/index.html')
    