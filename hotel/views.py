import os
from django.shortcuts import redirect, render
from .models import Destination,QuickBooking,Booking
from django.contrib import messages
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})

def booking(request):
    if request.method == 'POST':
        try:
            messages.info(request, 'Booked Sucessfully')
            return redirect('booking')
        except :
            messages.ERROR(request, 'Failed to book you room ')
            return redirect('booking')
    else:
        return render(request, 'booking.html')
    

"""name = request.POST['name']
            email = request.POST['email']
            checkINTime = request.POST['"check_in_dat']
            print(name, email, checkINTime) 
"""