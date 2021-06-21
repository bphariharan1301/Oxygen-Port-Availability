from django.urls.conf import path
from . import views

urlpatterns = [
    path('datasets', views.datasets, name='datasets'),
    # path('', include('pages.urls')), 
    
]  