from django.shortcuts import render

def index(request):
    return render(request, 'mi_app/index.html')  # Asegúrate de tener es

def about(request):
    return render(request, 'mi_app/about.html')

def contacto(request):  # Cambiado de 'contact' a 'contacto'
    return render(request, 'mi_app/contacto.html')

def menu_comida(request):
    return render(request, 'mi_app/menu_comida.html')

def menu_bebidas(request):
    return render(request, 'mi_app/menu_bebidas.html')