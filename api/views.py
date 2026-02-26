# api/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import District, Place
from .serializers import DistrictSerializer, PlaceSerializer, PlaceListSerializer

# ============================================
# SEARCH - FIXED VERSION
# ============================================
@api_view(['GET'])
def search_districts(request):
    """Search districts by name or tamil name"""
    try:
        # Get search query from URL parameter 'q'
        query = request.GET.get('q', '')
        
        print(f"🔍 Search query: '{query}'")  # Debug - check terminal
        
        # If query is empty or too short
        if not query or len(query) < 2:
            return Response([])
        
        # Search in name and tamil_name (case-insensitive)
        districts = District.objects.filter(
            Q(name__icontains=query) | 
            Q(tamil_name__icontains=query)
        )
        
        print(f"📊 Found: {districts.count()} districts")  # Debug
        
        # Serialize and return
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")  # Debug
        return Response({'error': str(e)}, status=500)


# ============================================
# DISTRICT VIEWS
# ============================================
@api_view(['GET'])
def get_all_districts(request):
    """Get all districts"""
    districts = District.objects.all()
    serializer = DistrictSerializer(districts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_district_by_id(request, district_id):
    """Get single district by ID"""
    district = get_object_or_404(District, id=district_id)
    serializer = DistrictSerializer(district)
    return Response(serializer.data)


@api_view(['GET'])
def get_district_by_path(request, path):
    """Get district by path (e.g., '/PdktDist')"""
    district = get_object_or_404(District, path=path)
    serializer = DistrictSerializer(district)
    return Response(serializer.data)


# ============================================
# PLACE VIEWS
# ============================================
@api_view(['GET'])
def get_all_places(request):
    """Get all places"""
    places = Place.objects.all()
    serializer = PlaceListSerializer(places, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_place_detail(request, place_id):
    """Get single place with full details"""
    place = get_object_or_404(Place, id=place_id)
    serializer = PlaceSerializer(place)
    return Response(serializer.data)


@api_view(['GET'])
def get_places_by_district(request, district_id):
    """Get all places in a specific district"""
    places = Place.objects.filter(district_id=district_id)
    serializer = PlaceListSerializer(places, many=True)
    return Response(serializer.data)


# ============================================
# HERO SLIDES (optional)
# ============================================
@api_view(['GET'])
def get_hero_slides(request):
    """Get hero slides for homepage"""
    # If you have HeroSlide model
    from .models import HeroSlide
    from .serializers import HeroSlideSerializer
    
    slides = HeroSlide.objects.all().select_related('place')
    serializer = HeroSlideSerializer(slides, many=True)
    return Response(serializer.data)