
from django import urls
from . import views
from django.urls.conf import include, path




urlpatterns = [
    path('contact-us', views.contact, name='contact-us'),
    # path('', include('pages.urls')), 
    
]  
