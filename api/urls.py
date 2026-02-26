# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # 🟢 SEARCH - MUST BE FIRST (before <int:district_id>)
    path('districts/search/', views.search_districts, name='search-districts'),
    
    # 🟢 DISTRICTS
    path('districts/', views.get_all_districts, name='all-districts'),
    path('districts/<int:district_id>/', views.get_district_by_id, name='district-by-id'),
    path('districts/path/<path:path>/', views.get_district_by_path, name='district-by-path'),
    
    # 🟢 PLACES BY DISTRICT
    path('districts/<int:district_id>/places/', views.get_places_by_district, name='district-places'),
    
    # 🟢 PLACES
    path('places/', views.get_all_places, name='all-places'),
    path('places/<int:place_id>/', views.get_place_detail, name='place-detail'),
    
    # 🟢 HERO SLIDES (if you have)
    path('hero-slides/', views.get_hero_slides, name='hero-slides'),
]