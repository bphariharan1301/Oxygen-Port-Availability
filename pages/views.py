from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def beds(request):

    beds_list = {
        'Name':'Hello',
    }
    
    return render(request, 'beds.html', {})

    
