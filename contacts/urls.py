
from . import views
from django.urls.conf import path


urlpatterns = [
    path('contact-us', views.contact, name='contact-us'),
    
]  
