from django.contrib import admin
from .models import Staff, CarouselImage, Product, DiveSite, Social

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('description', 'image')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cost')

@admin.register(DiveSite)
class DiveSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'citystateprov', 'country', 'map_url')

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
