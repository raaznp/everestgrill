from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("about", views.AboutUsView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("gallery/", views.GalleryView.as_view(), name="gallery"),
    path("menu/", views.MenuView.as_view(), name="menu"),
    path("reservation/", views.ReservationView.as_view(), name="reservation"),
]