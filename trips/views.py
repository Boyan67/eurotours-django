from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Trip, Month


def index(request):
    top_trips = Trip.objects.filter(top_offer=True)
    context = {'top_trips': top_trips}
    return render(request, '../templates/index.html', context)


def trips(request):
    all_trips = Trip.objects.all()
    context = {'all_trips': all_trips}
    return render(request, '../templates/trips.html', context)


def search(request):
    if request.method == "POST":
        search_box = request.POST.get('search')

        all_trips = []
        for i in Trip.objects.all():
            if search_box.lower() in i.name.lower():
                all_trips.append(i)
            elif search_box.lower() in i.text.lower():
                all_trips.append(i)

        context = {'search_box': search_box, 'all_trips': all_trips}
        return render(request, '../templates/trips.html', context)
    else:
        context = {}
        return render(request, '../templates/trips.html', context)


def trip_month(request, month_id):
    month = Month.objects.get(id=month_id)
    all_trips = Trip.objects.filter(months=month)
    context = {'all_trips': all_trips, 'month': month}
    return render(request, '../templates/trips.html', context)


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