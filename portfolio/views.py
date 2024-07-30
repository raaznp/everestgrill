from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from . models import Menu, AboutUs, Contact, Gallery, Menu, Reservation, HomeSlider
# Create your views here.


class IndexView(TemplateView):
    template_name = "theme/index.html"
    
class AboutUsView(ListView):
    model = AboutUs
    template_name = "theme/about_us.html"

class ContactView(ListView):
    model = Contact
    template_name = "theme/contact.html"

class GalleryView(ListView):
    model = Gallery
    template_name = "theme/gallery.html"

class MenuView(ListView):
    model = Menu
    template_name = "theme/menu1.html"

class ReservationView(ListView):
    model = Reservation
    template_name = "theme/reservation.html"

class HomeSliderView(ListView):
    model = HomeSlider
    template_name = "theme/index.html"