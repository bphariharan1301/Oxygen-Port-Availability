
from django.urls import path
from . import views

urlpatterns = [
    path('oxygen', views.oxygen, name='oxygen'),
    path('contact', views.contact, name='contact'),
]
