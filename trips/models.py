from django.db import models
from multiselectfield import MultiSelectField
from tinymce import models as tinymce_models

month = [('01', 'January'),
         ('02', 'February'),
         ('03', 'March'),
         ('04', 'April'),
         ('05', 'May'),
         ('06', 'June'),
         ('07', 'July'),
         ('08', 'August'),
         ('09', 'September'),
         ('10', 'October'),
         ('11', 'November'),
         ('12', 'December')]

categories = [
    ('overnight', 'Overnight'),
    ('shopping', 'Shopping'),
    ('food included', 'Food Included'),
    ('excursion', 'Excursion'),
    ('for students', 'For Students'),
    ('holiday', 'Holiday')
]


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Month(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Trip(models.Model):
    top_offer = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='main_images/')
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    duration = models.CharField(max_length=50, default="1 нощувка")
    country = models.CharField(max_length=50)
    months = models.ManyToManyField(Month)
    text = tinymce_models.HTMLField()


class Image(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/')



