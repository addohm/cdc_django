from django.db import models
from cdc_project.settings import STATIC_URL

images_url = STATIC_URL + 'images/'

class Staff(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=images_url + 'staff/')
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CarouselImage(models.Model):
    image = models.ImageField(upload_to=images_url + 'carousel/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.description or f"Image {self.id}"

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.CharField(max_length=8)

    def __str__(self):
        return self.title
    
class DiveSite(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    country = models.CharField(max_length=255)
    citystateprov = models.CharField(max_length=255)
    map_url = models.URLField(max_length=255)
    image = models.ImageField(upload_to=images_url + 'sites/')

    def __str__(self):
        return self.name

class Social(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    image = models.ImageField(upload_to=images_url + 'socials/')

    def __str__(self):
        return self.name