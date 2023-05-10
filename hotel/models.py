from django.db import models

# Create your models here.
class Destination(models.Model):
   img = models.ImageField(upload_to='pics')
   suite = models.CharField(max_length=100)
   price = models.IntegerField()
   desc = models.TextField()
   booking = models.BooleanField(default=False)


class QuickBooking(models.Model):
   checkin = models.DateTimeField()
   checkout = models.DateTimeField()
   adult_no = models.CharField(max_length=50)
   child_no = models.CharField(max_length=50)

class Booking(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField()
   checkin = models.DateTimeField()
   checkout = models.DateTimeField()
   adult_no = models.CharField(max_length=50)
   child_no = models.CharField(max_length=50)
   room = models.BooleanField()
   special_request = models.TextField()