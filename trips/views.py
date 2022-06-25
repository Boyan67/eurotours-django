from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Trip


def index(request):
    top_trips = Trip.objects.filter(top_offer=True)
    context = {'top_trips': top_trips}
    return render(request, '../templates/index.html', context)


def trips(request):
    top_trips = Trip.objects.all()
    context = {'top_trips': top_trips}
    return render(request, '../templates/trips-simple.html', context)


def trip_details(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    context = {'trip': trip}
    return render(request, '../templates/details.html', context)


def about(request):
    return HttpResponse("ABOUT.")


def contact(request):
    return HttpResponse("CONTACT.")


def conditions(request):
    return HttpResponse("CONDITIONS.")