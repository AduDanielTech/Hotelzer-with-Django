from django.contrib import admin
from .models import Destination, Booking, QuickBooking

# Register your models here.
admin.site.register(Destination),
admin.site.register(Booking),
admin.site.register(QuickBooking)
