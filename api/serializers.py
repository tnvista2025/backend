# api/serializers.py

from rest_framework import serializers
from .models import District, Place, HeroSlide

class DistrictSerializer(serializers.ModelSerializer):
    """Serializer for District model - matches your frontend data structure"""
    
    class Meta:
        model = District
        fields = ['id', 'name', 'tamil_name', 'image', 'path', 'essence', 'specialty']

class PlaceSerializer(serializers.ModelSerializer):
    """Serializer for Place model"""
    district_name = serializers.CharField(source='district.name', read_only=True)
    
    class Meta:
        model = Place
        fields = '__all__'

class PlaceListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for listing places"""
    
    class Meta:
        model = Place
        fields = ['id', 'name', 'location', 'hero_image', 'tagline', 'district_id']

class HeroSlideSerializer(serializers.ModelSerializer):
    """Serializer for hero slides"""
    place_id = serializers.IntegerField(source='place.id')
    place_name = serializers.CharField(source='place.name')
    place_location = serializers.CharField(source='place.location')
    place_tagline = serializers.CharField(source='place.tagline')
    place_image = serializers.URLField(source='place.hero_image')
    
    class Meta:
        model = HeroSlide
        fields = ['id', 'place_id', 'place_name', 'place_location', 
                  'place_tagline', 'place_image', 'custom_name', 
                  'custom_tagline', 'order']