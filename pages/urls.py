
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('beds', views.beds, name='beds'),
    path('search', views.search, name='search'),
    path('oxygen', views.oxygen, name='oxygen'),
    # path('charts', views.charts, name='charts'),
    path('donate', views.donate, name='donate'),
    path('error_page', views.error_page, name='error_page'),
]
