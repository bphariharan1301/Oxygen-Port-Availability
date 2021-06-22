from pages.models import Hospital
from django.shortcuts import render
from .choices import *

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def beds(request):    
    
    hospitals = Hospital.objects.all() 
    # queryset_list = Hospital.objects.all() 

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            hospitals = hospitals.filter(state__iexact=state)
            # queryset_list = queryset_list.filter(statet=state__iexact)
    
    if 'district' in request.GET:
        state = request.GET['district']
        if state:
            hospitals = hospitals.filter(state__iexact=state)
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
    return render(request, 'beds.html', context)

def oxygen(request):
    return render(request, 'oxygens.html', {})

# def charts(request):
#     return render(request, 'Charts.html', {})

def donate(request):
    return render(request, 'Donate.html', {})


