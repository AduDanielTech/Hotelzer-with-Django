import os
from django.shortcuts import redirect, render
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
            messages.info(request, 'Booked Sucessfully')
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
    

"""name = request.POST['name']
            email = request.POST['email']
            checkINTime = request.POST['"check_in_dat']
            print(name, email, checkINTime) 
"""