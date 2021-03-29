from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def blogsingle(request):
    return render(request, 'core/blog-single.html')

def blog(request):
    return render(request, 'core/blog.html')

def contact(request):
    return render(request, 'core/contact.html')

def menu(request):
    return render(request, 'core/menu.html')

def plantilla (request):
    return render(request, 'core/plantilla.html')

def services(request):
    return render(request, 'core/services.html')
    