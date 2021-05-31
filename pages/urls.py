
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('beds', views.beds, name='beds'),
    path('oxygen', views.oxygen, name='oxygen'),
    path('contact', views.contact, name='contact'),
    path('charts', views.charts, name='charts'),
    path('donate', views.donate, name='donate'),
]
