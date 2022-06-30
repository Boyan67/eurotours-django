from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trips/', views.trips, name='trips'),
    path('trip/<int:trip_id>', views.trip_details, name='trip_details'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('conditions/', views.conditions, name='conditions'),
]
