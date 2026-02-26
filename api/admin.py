# api/admin.py

from django.contrib import admin
from .models import District, Place, HeroSlide

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tamil_name', 'essence']
    search_fields = ['name', 'tamil_name']
    list_filter = ['essence']

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'district', 'location']
    search_fields = ['name', 'district__name']
    list_filter = ['district', 'is_featured']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('district', 'name', 'location', 'tagline')
        }),
        ('Media', {
            'fields': ('hero_image', 'gallery_images')
        }),
        ('Details', {
            'fields': ('history', 'deity', 'timings', 'best_month', 'festivals', 'reach')
        }),
        ('Architecture', {
            'fields': ('architecture',)
        }),
        ('Metadata', {
            'fields': ('is_featured',)
        }),
    )

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ['id', 'place', 'order']
    list_editable = ['order']