from django.shortcuts import render, redirect
from . models import Bus, Booking
from datetime import datetime
from . city import Cities
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    buses = Bus.objects.all()
    context = {
        'buses': buses,
        'cities':Cities
    }
    return render(request, 'pages/index.html', context)

def search_results(request):
    fromcity = request.GET['fromcity']
    tocity = request.GET['tocity']
    date = request.GET['date']
    
    buses = Bus.objects.filter(from_city=fromcity,to_city=tocity, date=date, no_of_seats__gte=1, date__gte=datetime.today())
    context = {
        'buses': buses
    }
    return render(request, 'pages/search_result.html', context)

@login_required(login_url='login')  
def reserve(request, id):
    bus = get_object_or_404(Bus, id=id)
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        booking = Booking.objects.create(
            user = request.user,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            email = email,
            bus_no = bus.bus_no,
            from_city = bus.from_city,
            to_city = bus.to_city,
            price = bus.price,
            date = bus.date,
            time = bus.time,
            bus = bus
        )
        booking.save()
        bus.no_of_seats -= 1
        bus.save()
        return redirect('bookings')
    context = {
        'bus' : bus
    }
    return render(request, 'pages/bookingform.html',  context)

def cancel_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    bus = Bus.objects.get(booking__id= id)
    bus.no_of_seats += 1
    bus.save()
    Booking.delete(booking)
    print(bus)
    return redirect('bookings')

def update(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        Booking.objects.filter(id = id).update(first_name = first_name, last_name = last_name, phone = phone, email = email)
        return redirect('bookings')
    else:
        context = {
            'booking':booking
        }
        return render(request, 'pages/update.html', context)