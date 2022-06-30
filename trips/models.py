import sys

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from tinymce import models as tinymce_models
from io import BytesIO
from PIL import Image
from django.core.files import File
from copy import deepcopy


# image compression method
def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


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
    category = models.ManyToManyField(Category)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    duration = models.CharField(max_length=50, default="1 нощувка")
    country = models.CharField(max_length=50)
    months = models.ManyToManyField(Month)
    text = tinymce_models.HTMLField()

    def save(self, *args, **kwargs):
        im = Image.open(self.main_image)
        im_io = BytesIO()
        im.save(im_io, 'JPEG', quality=50)
        self.main_image = InMemoryUploadedFile(im_io, 'ImageField', "%s.jpg" % self.main_image.name.split('.')[0],
                                               'main_images/', sys.getsizeof(im_io), None)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Екскурзия/Почивка"
        verbose_name_plural = "Екскурзии и Почивки"


class Picture(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        im = Image.open(self.image)
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        im_io = BytesIO()
        bg.save(im_io, 'JPEG', quality=80)
        self.image = InMemoryUploadedFile(im_io, 'ImageField', "%s.jpg" % self.image.name.split('.')[0],
                                          'images/', sys.getsizeof(im_io), None)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.trip.name} - {self.name}"

    class Meta:
        verbose_name = "Снимка"
        verbose_name_plural = "Снимки"


class HomeImage(models.Model):
    home_image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        if not self.pk and HomeImage.objects.exists():
            raise ValidationError('Може да има само една начална снимка')
        return super(HomeImage, self).save(*args, **kwargs)

    def __str__(self):
        return "Начален Екран - Снимка"

    class Meta:
        verbose_name = "Начален Екран - Снимка"
        verbose_name_plural = "Начален Екран - Снимка"


class Condition(models.Model):
    name = models.CharField(max_length=200)
    document = models.FileField(upload_to='documents/')
    text = tinymce_models.HTMLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Условия и Документи"