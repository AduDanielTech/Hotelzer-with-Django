from django.forms import ModelForm
from django import forms
from .models import QuickBooking
class QuickBookingForm(ModelForm):
   checkin = forms.DateTimeField()
   checkout = forms.DateTimeField()
   adult_no = forms.Select()
   child_no = forms.Select()
   class Meta:
      model = QuickBooking
      fields = ['checkin','checkout','adult_no','child_no',]
      
    
