from pages.models import Hospital
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def beds(request): 
    hospitals = Hospital.objects.all() 
    context = {'hospitals':hospitals}
    # return render(request, 'beds.html', {'hospitals':hospitals}) You can pass in this way too!
    return render(request, 'beds.html', context)

def oxygen(request):
    return render(request, 'oxygens.html', {})

# def contact(request):
#     return render(request, 'Contact.html', {})

def charts(request):
    return render(request, 'Charts.html', {})

def donate(request):
    return render(request, 'Donate.html', {})


