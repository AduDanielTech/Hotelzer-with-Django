import os
from django.shortcuts import redirect, render

from hotel.forms import QuickBookingForm
from .models import Destination,QuickBooking,Booking
from django.contrib.auth.models import auth
from django.contrib import messages
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})

def booking(request):
    if request.method == 'POST':
        try:
            try:
                form = QuickBookingForm(request.POST)
                if form.is_valid():
                    form.save()
                else:
                    messages.error(request, 'Booking failed')
                print(request.POST)
                messages.info(request, 'Booked Sucessfully')
            except:
                messages.error(request, 'Booking failed')
            return redirect('booking')
        except :
            messages.ERROR(request, 'Failed to book you room ')
            return redirect('booking')
    else:
        if request.user.is_authenticated:
            return render(request, 'booking.html')
        else:
            return  redirect('accounts/login')



def about(request):
    return render(request, 'about.html')
    

def services(request):
    return render(request, 'service.html')

def room(request):
    return render(request, 'room.html')
    
def contact(request):
    return render(request, 'contact.html')
    

"""name = request.POST['name']
            email = request.POST['email']
            checkINTime = request.POST['"check_in_dat']
            print(name, email, checkINTime) 
"""