from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ,name='index'),
    path('booking' ,views.booking , name='booking'),
    path('about' ,views.about , name='about'),
    path('services' ,views.services , name='services'),
    path('room' ,views.room , name='room'),
    path('contact' ,views.contact , name='contact'),
    ]