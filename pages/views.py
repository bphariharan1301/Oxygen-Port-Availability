from pages.models import Hospital
from django.shortcuts import render
from .choices import *

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def search(request):    
    
    hospitals = Hospital.objects.all() 
    # queryset_list = Hospital.objects.all() 

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            hospitals = hospitals.filter(state__iexact=state)
            # queryset_list = queryset_list.filter(statet=state__iexact)
    
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            hospitals = hospitals.filter(district__iexact=district)
            # queryset_list = queryset_list.filter(statet=state__iexact)

    # print(state)

    context = {
        'hospitals':hospitals,
        # 'hospitals':queryset_list,
        'state_choices': state_choices,
        'values':request.GET

    }

    # print(hospitals)

    # return render(request, 'beds.html', {'hospitals':hospitals}) You can pass in this way too!
    return render(request, 'search.html', context)

def beds(request):
    return render(request, 'beds.html')

def oxygen(request):
    return render(request, 'oxygens.html', {})

def donate(request):
    return render(request, 'Donate.html', {})

def error_page(request):
    return render(request, 'partials/_page404.html')


