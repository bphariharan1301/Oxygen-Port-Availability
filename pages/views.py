from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def beds(request):    
    return render(request, 'beds.html', {})

def oxygen(request):
    return render(request, 'oxygens.html', {})

def contact(request):
    return render(request, 'Contact.html', {})

def charts(request):
    return render(request, 'Charts.html', {})

def donate(request):
    return render(request, 'Donate.html', {})


