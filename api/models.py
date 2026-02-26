# api/models.py

from django.db import models

class District(models.Model):
    """Model for Tamil Nadu Districts"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tamil_name = models.CharField(max_length=100)
    image = models.URLField(max_length=500)  # Using URL for images (Supabase)
    path = models.CharField(max_length=100)  # Route path
    essence = models.CharField(max_length=200)  # "Land of 1000+ Temples"
    specialty = models.CharField(max_length=200)  # "Chettinad Architecture"
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Place(models.Model):
    """Model for Places/Attractions in each district"""
    id = models.AutoField(primary_key=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='places')
    
    # Basic Info
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    tagline = models.TextField(blank=True, null=True)
    
    # Media
    hero_image = models.URLField(max_length=500)
    gallery_images = models.JSONField(default=list)  # Store array of URLs
    
    # Details
    history = models.TextField()
    deity = models.CharField(max_length=200, blank=True, null=True)
    timings = models.CharField(max_length=200, blank=True, null=True)
    best_month = models.CharField(max_length=200, blank=True, null=True)
    festivals = models.JSONField(default=list)  # Store array of festival names
    reach = models.TextField(blank=True, null=True)
    
    # Architecture/Heritage
    architecture = models.TextField(blank=True, null=True)
    
    # Metadata
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.district.name}"

class HeroSlide(models.Model):
    """For homepage hero slides"""
    id = models.AutoField(primary_key=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='hero_slides')
    
    # Override fields if needed (otherwise use place data)
    custom_name = models.CharField(max_length=200, blank=True, null=True)
    custom_tagline = models.TextField(blank=True, null=True)
    
    # Order
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"Hero: {self.place.name}"