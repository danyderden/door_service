from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    return render(request, 'products.html')


def store(request):
    return render(request, 'contacts.html')
