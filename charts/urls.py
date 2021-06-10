
from . import views
from django.urls.conf import path


urlpatterns = [
    path('charts', views.charts, name='charts'),
    
]  
