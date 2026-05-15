from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

from .models import Service, Category


def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    
    return render(request, 'fixalbania/home.html', context)


def services(request):
    services = Service.objects.all()
    categories = Category.objects.all()
    context = {
        'services': services,
        'categories': categories
    }
    
    return render(request, 'fixalbania/services.html', context)


def about_us(request):
    context = {}
    
    return render(request, 'fixalbania/about_us.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # save or process form here
            return redirect('success')

    else:
        form = ContactForm()

    context = {'form': form}

    return render(request, 'fixalbania/contact.html', context)