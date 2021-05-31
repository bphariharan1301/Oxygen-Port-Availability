from django.shortcuts import render

# Create your views here.

def oxygen(request):
    return render(request, 'oxygens.html', {})

def contact(request):
    return render(request, 'Contact.html', {})
