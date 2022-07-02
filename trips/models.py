import os
import sys

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.dispatch import receiver
from tinymce import models as tinymce_models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db.models.signals import pre_save
from .storage import OverwriteStorage
import os


# image compression method
def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Month(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Trip(models.Model):
    top_offer = models.BooleanField(default=False, verbose_name="Топ Оферта")
    name = models.CharField(max_length=200, verbose_name="Име")
    main_image = models.ImageField(upload_to='main_images/', verbose_name="Главна Снимка")
    category = models.ManyToManyField(Category, verbose_name="Категории")
    price = models.IntegerField(verbose_name="Цена")
    duration = models.CharField(max_length=50, default="1 нощувка", verbose_name="Пордължителнот")
    country = models.CharField(max_length=50, verbose_name="Държава")
    months = models.ManyToManyField(Month, verbose_name="През Месеци:")
    text = tinymce_models.HTMLField(verbose_name="Текст")

    def save(self, *args, **kwargs):
        im = Image.open(self.main_image)
        im_io = BytesIO()
        im.save(im_io, 'JPEG', quality=50)
        # im.close()
        self.main_image.close()

        new_image = File(im_io, name=self.main_image.name.split("/")[-1])
        self.main_image = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Екскурзия/Почивка"
        verbose_name_plural = "Екскурзии и Почивки"


class Picture(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name="Екскурзия/Почивка")
    name = models.CharField(max_length=200, blank=True, verbose_name="Име за снимката")
    image = models.ImageField(upload_to='images/', verbose_name="Снимка")

    def save(self, *args, **kwargs):
        im = Image.open(self.image)
        im_io = BytesIO()
        im.save(im_io, 'JPEG', quality=80)
        # im.close()
        self.image.close()

        new_image = File(im_io, name=f"{self.trip.name}/{self.image.name.split('/')[-1]}")
        self.image = new_image
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.trip.name} - {self.name}"

    class Meta:
        verbose_name = "Снимка"
        verbose_name_plural = "Снимки"


class HomeImage(models.Model):
    home_image = models.ImageField(upload_to='images/', verbose_name="Снимка на Началният Екран")

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
    name = models.CharField(max_length=200, verbose_name="Име на Документа")
    document = models.FileField(upload_to='documents/', verbose_name="Документ", blank=True)
    text = tinymce_models.HTMLField(verbose_name="Текст")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Условия и Документи"
