from django.db import models
from .validators import validate_image

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=99)
    team_position = models.CharField(max_length=99)
    team_image = models.ImageField(
        upload_to='media/uploads/team/',
        null=True,
        blank=True,
        default='media/uploads/team/default.png',
        verbose_name='Team Image',
        help_text='Upload a team image',
        validators=[validate_image],
        error_messages={
            'invalid': "Image files only",
            'missing': "No image file was found",
            'empty': "Please upload an image file",
            'invalid_image': "Upload a valid image. The file you uploaded was either not an image or a corrupted image.",
            'max_length': "This image has a very large file size. Please upload an image with a smaller file size.",
        }
    )

class AboutUs(models.Model):
    about_us = models.TextField()
    about_us_image = models.ImageField()

class Contact(models.Model):
    contact_address = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    contact_map = models.TextField()

class Gallery(models.Model):
    gallery_image = models.ImageField()

class Menu(models.Model):
    menu_name = models.CharField(max_length=99)
    menu_detail = models.CharField(max_length=999)
    menu_price = models.PositiveIntegerField()
    menu_image = models.ImageField(
        upload_to='media/uploads/menu/',
        null=True,
        blank=True,
        default='media/uploads/menu/default.jpg',
        verbose_name='Menu Image',
        help_text='Upload a menu image',
        validators=[validate_image],
        error_messages={
            'invalid': "Image files only",
            'missing': "No image file was found",
            'empty': "Please upload an image file",
            'invalid_image': "Upload a valid image. The file you uploaded was either not an image or a corrupted image.",
            'max_length': "This image has a very large file size. Please upload an image with a smaller file size.",
        }
    )

class Reservation(models.Model):
    reservation_name = models.CharField(max_length=255)
    reservation_email = models.EmailField()
    reservation_phone = models.CharField(max_length=15)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    reservation_guests = models.PositiveIntegerField()

class Testimonial(models.Model):
    testimonial_name = models.CharField(max_length=255)
    testimonial_details = models.TextField()
    testimonial_image = models.ImageField(
        upload_to='media/uploads/testimonial/',
        null=True,
        blank=True,
        default='media/uploads/testimonial/default.png',
        verbose_name='Testimonial Image',
        help_text='Upload a testimonial image',
        validators=[validate_image],
        error_messages={
            'invalid': "Image files only",
            'missing': "No image file was found",
            'empty': "Please upload an image file",
            'invalid_image': "Upload a valid image. The file you uploaded was either not an image or a corrupted image.",
            'max_length': "This image has a very large file size. Please upload an image with a smaller file size.",
        }
    )
    testimonial_position = models.CharField(max_length=255, null = True, blank = True)
    testimonial_company = models.CharField(max_length=255, null = True, blank = True)

class HomeSlider(models.Model):
    slider_image = models.ImageField(
        upload_to='media/uploads/slider/',
        null=True,
        blank=True,
        default='media/uploads/slider/default.png',
        verbose_name='Team Image',
        help_text='Upload a team image',
        validators=[validate_image],
        error_messages={
            'invalid': "Image files only",
            'missing': "No image file was found",
            'empty': "Please upload an image file",
            'invalid_image': "Upload a valid image. The file you uploaded was either not an image or a corrupted image.",
            'max_length': "This image has a very large file size. Please upload an image with a smaller file size.",
        }
    )
    slider_title = models.CharField(max_length=255)
    slider_description = models.TextField(max_length=1500)