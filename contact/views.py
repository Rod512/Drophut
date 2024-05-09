from django.shortcuts import render
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            'message from' + name,
            message, 
            email, #from email
            ['rudrodhar46@gmail.com'], #to email
        )
        return render(request, 'contact/contact.html',{'message': message})
    else:
        return render(request, 'contact/contact.html',)