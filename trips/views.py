from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .filters import TripFilter
from .models import Trip, Month, Category


def index(request):
    top_trips = Trip.objects.filter(top_offer=True)
    context = {'top_trips': top_trips}
    return render(request, '../templates/index.html', context)


def trips(request):
    search_box = ""
    all_trips = Trip.objects.all()
    my_filter = TripFilter(request.GET, queryset=all_trips)
    all_trips = my_filter.qs

    if request.method == "POST":
        if request.POST.get('search'):
            search_box = request.POST.get('search')
            all_trips = []
            for i in Trip.objects.all():
                if search_box.lower() in i.name.lower():
                    all_trips.append(i)
                elif search_box.lower() in i.text.lower():
                    all_trips.append(i)
        if request.POST.get('month'):
            month = Month.objects.get(name=request.POST.get('month'))
            all_trips = Trip.objects.filter(months=month)
        if request.POST.get('category'):
            category = Category.objects.get(name=request.POST.get('category'))
            all_trips = Trip.objects.filter(category=category)

    context = {'all_trips': all_trips, 'my_filter': my_filter, 'search_box': search_box}
    return render(request, '../templates/trips.html', context)


def trip_month(request, month_id):
    month = Month.objects.get(id=month_id)
    all_trips = Trip.objects.filter(months=month)

    if request.method == "GET":
        all_trips = Trip.objects.all()
        my_filter = TripFilter(request.GET, queryset=all_trips)
        all_trips = my_filter.qs
        context = {'all_trips': all_trips, 'my_filter': my_filter}
        return render(request, '../templates/trips.html', context)

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