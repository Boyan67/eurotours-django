from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .filters import TripFilter
from .models import Trip, Month, Category, HomeImage, Condition, Picture


def index(request):
    top_trips = Trip.objects.filter(top_offer=True)
    home_image = HomeImage.objects.first()
    context = {'top_trips': top_trips, 'home_image':home_image}
    return render(request, '../templates/index.html', context)


def trips(request):
    search_box = ""
    all_trips = Trip.objects.all()
    my_filter = TripFilter(request.GET, queryset=all_trips)
    all_trips = my_filter.qs
    month = ""
    category = ""

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

    context = {'all_trips': all_trips, 'my_filter': my_filter, 'search_box': search_box,
               'month': month, 'category': category}
    return render(request, '../templates/trips.html', context)


def trip_details(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    images = Picture.objects.filter(trip=trip)

    context = {'trip': trip, 'images':images, 'iterateover': range(len(images)-2)}
    print(range(len(images)-2))
    return render(request, '../templates/trip-detail.html', context)


def about(request):
    return render(request, '../templates/about.html')


def contact(request):
    return render(request, '../templates/contact.html')


def conditions(request):
    usloviq = Condition.objects.all()
    context = {'usloviq': usloviq}
    return render(request, '../templates/usloviq.html', context)
