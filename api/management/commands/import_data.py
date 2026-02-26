# api/management/commands/import_data.py

from django.core.management.base import BaseCommand
from api.models import District, Place
import json

class Command(BaseCommand):
    help = 'Import districts and places from hardcoded data to PostgreSQL'
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🚀 Starting data import...'))
        
        # ============================================
        # STEP 1: IMPORT DISTRICTS (38 Districts)
        # ============================================
        self.import_districts()
        
        # ============================================
        # STEP 2: IMPORT PLACES
        # ============================================
        self.import_places()
        
        self.stdout.write(self.style.SUCCESS('✅ Data import completed successfully!'))
    
    def import_districts(self):
        """Import all 38 districts from your DistrictPage.jsx"""
        
        districts_data = [
            {
                "id": 1,
                "name": "Pudukkottai",
                "tamil_name": "புதுக்கோட்டை",
                "image": "https://jeiwwgoxuldwoxurkalo.supabase.co/storage/v1/object/sign/tnvista/pudukkottai/kundandarkovil/kunext2.jpg",
                "path": "/PdktDist",
                "essence": "Land of 1000+ Temples",
                "specialty": "Chettinad Architecture"
            },
            {
                "id": 2,
                "name": "Madurai",
                "tamil_name": "மதுரை",
                "image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Meenachiamman-temple/meenachiamman6.jpg",
                "path": "/MaduraiDist",
                "essence": "City of Festivals",
                "specialty": "Meenakshi Temple"
            },
            {
                "id": 3,
                "name": "Chennai",
                "tamil_name": "சென்னை",
                "image": "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=500",
                "path": "/ChennaiDist",
                "essence": "Gateway to South India",
                "specialty": "Marina Beach"
            },
            {
                "id": 4,
                "name": "Coimbatore",
                "tamil_name": "கோயம்புத்தூர்",
                "image": "https://images.unsplash.com/photo-1615870216519-2f9fa575fa7c?w=500",
                "path": "/CoimbatoreDist",
                "essence": "Manchester of South",
                "specialty": "Textile Hub"
            },
            {
                "id": 5,
                "name": "Thanjavur",
                "tamil_name": "தஞ்சாவூர்",
                "image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/Thanjavur/Big%20Temple/unnamed.webp",
                "path": "/ThanjavurDist",
                "essence": "Land of Chola Legacy",
                "specialty": "Brihadeeswarar Temple"
            },
            {
                "id": 6,
                "name": "Kanyakumari",
                "tamil_name": "கன்னியாகுமரி",
                "image": "https://images.unsplash.com/photo-1589908805464-86517c13d1e1?w=500",
                "path": "/KanyakumariDist",
                "essence": "Where Three Seas Meet",
                "specialty": "Vivekananda Rock"
            },
            {
                "id": 7,
                "name": "Ooty",
                "tamil_name": "ஊட்டி",
                "image": "https://images.unsplash.com/photo-1626621331446-7c6a5e8e5b5b?w=500",
                "path": "/OotyDist",
                "essence": "Queen of Hills",
                "specialty": "Tea Plantations"
            },
            {
                "id": 8,
                "name": "Rameswaram",
                "tamil_name": "இராமேஸ்வரம்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/RameswaramDist",
                "essence": "Sacred Island",
                "specialty": "Pamban Bridge"
            },
            {
                "id": 9,
                "name": "Kanchipuram",
                "tamil_name": "காஞ்சிபுரம்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/KanchipuramDist",
                "essence": "City of Thousand Temples",
                "specialty": "Silk Sarees"
            },
            {
                "id": 10,
                "name": "Tiruchirappalli",
                "tamil_name": "திருச்சிராப்பள்ளி",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/TrichyDist",
                "essence": "Rockfort City",
                "specialty": "Rockfort Temple"
            },
            {
                "id": 11,
                "name": "Vellore",
                "tamil_name": "வேலூர்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/VelloreDist",
                "essence": "Fort City",
                "specialty": "Golden Temple"
            },
            {
                "id": 12,
                "name": "Salem",
                "tamil_name": "சேலம்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/SalemDist",
                "essence": "Mango City",
                "specialty": "Steel Plant"
            },
            {
                "id": 13,
                "name": "Tirunelveli",
                "tamil_name": "திருநெல்வேலி",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/TirunelveliDist",
                "essence": "Halwa City",
                "specialty": "Courtallam Falls"
            },
            {
                "id": 14,
                "name": "Erode",
                "tamil_name": "ஈரோடு",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/ErodeDist",
                "essence": "Turmeric City",
                "specialty": "Bhavani River"
            },
            {
                "id": 15,
                "name": "Dindigul",
                "tamil_name": "திண்டுக்கல்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/DindigulDist",
                "essence": "Lock City",
                "specialty": "Dindigul Biryani"
            },
            {
                "id": 16,
                "name": "Namakkal",
                "tamil_name": "நாமக்கல்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/NamakkalDist",
                "essence": "Egg City",
                "specialty": "Namakkal Fort"
            },
            {
                "id": 17,
                "name": "Karur",
                "tamil_name": "கருர்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/KarurDist",
                "essence": "Home Textile Hub",
                "specialty": "Amaravathi River"
            },
            {
                "id": 18,
                "name": "Perambalur",
                "tamil_name": "பெரம்பலூர்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/PerambalurDist",
                "essence": "Fossils Hub",
                "specialty": "Ranaganathar Temple"
            },
            {
                "id": 19,
                "name": "Ariyalur",
                "tamil_name": "அரியலூர்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/AriyalurDist",
                "essence": "Cement City",
                "specialty": "Fossils"
            },
            {
                "id": 20,
                "name": "Cuddalore",
                "tamil_name": "கடலூர்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/CuddaloreDist",
                "essence": "Port City",
                "specialty": "Silver Beach"
            },
            {
                "id": 21,
                "name": "Villupuram",
                "tamil_name": "விழுப்புரம்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/VillupuramDist",
                "essence": "Agricultural Hub",
                "specialty": "Gingee Fort"
            },
            {
                "id": 22,
                "name": "Ranipet",
                "tamil_name": "ராணிப்பேட்டை",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/RanipetDist",
                "essence": "Industrial Town",
                "specialty": "Leather Hub"
            },
            {
                "id": 23,
                "name": "Tirupathur",
                "tamil_name": "திருப்பத்தூர்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/TirupathurDist",
                "essence": "Javadi Hills",
                "specialty": "Yelagiri"
            },
            {
                "id": 24,
                "name": "Krishnagiri",
                "tamil_name": "கிருஷ்ணகிரி",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/KrishnagiriDist",
                "essence": "Mango Hub",
                "specialty": "Hogenakkal"
            },
            {
                "id": 25,
                "name": "Dharmapuri",
                "tamil_name": "தர்மபுரி",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/DharmapuriDist",
                "essence": "Gateway to Hills",
                "specialty": "Theerthamalai"
            },
            {
                "id": 26,
                "name": "Tiruvannamalai",
                "tamil_name": "திருவண்ணாமலை",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/TiruvannamalaiDist",
                "essence": "Spiritual City",
                "specialty": "Arunachala Hill"
            },
            {
                "id": 27,
                "name": "Kallakurichi",
                "tamil_name": "கள்ளக்குறிச்சி",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/KallakurichiDist",
                "essence": "Agricultural Belt",
                "specialty": "Kallakurichi Rice"
            },
            {
                "id": 28,
                "name": "Chengalpattu",
                "tamil_name": "செங்கல்பட்டு",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/ChengalpattuDist",
                "essence": "Temple Gateway",
                "specialty": "Mahabalipuram"
            },
            {
                "id": 29,
                "name": "Thoothukkudi",
                "tamil_name": "தூத்துக்குடி",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/ThoothukkudiDist",
                "essence": "Pearl City",
                "specialty": "Port"
            },
            {
                "id": 30,
                "name": "Ramanathapuram",
                "tamil_name": "இராமநாதபுரம்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/RamanathapuramDist",
                "essence": "Maritime Heritage",
                "specialty": "Pamban Bridge"
            },
            {
                "id": 31,
                "name": "Sivagangai",
                "tamil_name": "சிவகங்கை",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/SivagangaiDist",
                "essence": "Queen's Land",
                "specialty": "Maruthu Pandiyar"
            },
            {
                "id": 32,
                "name": "Virudhunagar",
                "tamil_name": "விருதுநகர்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/VirudhunagarDist",
                "essence": "Match City",
                "specialty": "Fireworks"
            },
            {
                "id": 33,
                "name": "Tenkasi",
                "tamil_name": "தென்காசி",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/TenkasiDist",
                "essence": "Temple Town",
                "specialty": "Courtallam Falls"
            },
            {
                "id": 34,
                "name": "Nilgiris",
                "tamil_name": "நீலகிரி",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/NilgirisDist",
                "essence": "Blue Mountains",
                "specialty": "Tea Gardens"
            },
            {
                "id": 35,
                "name": "Tiruppur",
                "tamil_name": "திருப்பூர்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/TiruppurDist",
                "essence": "Knitwear City",
                "specialty": "Textile Export"
            },
            {
                "id": 36,
                "name": "Mayiladuthurai",
                "tamil_name": "மயிலாடுதுறை",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/MayiladuthuraiDist",
                "essence": "Temple Town",
                "specialty": "Cauvery Delta"
            },
            {
                "id": 37,
                "name": "Nagapattinam",
                "tamil_name": "நாகப்பட்டினம்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/NagapattinamDist",
                "essence": "Port Town",
                "specialty": "Velankanni"
            },
            {
                "id": 38,
                "name": "Thiruvarur",
                "tamil_name": "திருவாரூர்",
                "image": "https://images.unsplash.com/photo-1622128377979-48521cb1a4bd?w=500",
                "path": "/ThiruvarurDist",
                "essence": "Temple City",
                "specialty": "Thyagaraja Temple"
            }
        ]
        
        self.stdout.write("📥 Importing 38 districts...")
        
        for dist_data in districts_data:
            # update_or_create - ஏற்கனவே இருந்தால் update பண்ணும், இல்லைனா create பண்ணும்
            district, created = District.objects.update_or_create(
                id=dist_data['id'],  # ID வைத்து find பண்ணும்
                defaults={
                    'name': dist_data['name'],
                    'tamil_name': dist_data['tamil_name'],
                    'image': dist_data['image'],
                    'path': dist_data['path'],
                    'essence': dist_data['essence'],
                    'specialty': dist_data['specialty'],
                }
            )
            
            if created:
                self.stdout.write(f"  ✅ Created: {district.name}")
            else:
                self.stdout.write(f"  🔄 Updated: {district.name}")
        
        self.stdout.write(self.style.SUCCESS(f"✅ {len(districts_data)} districts imported successfully!"))
    
    def import_places(self):
        """Import all places from your PdktDetails.jsx, MaduraiDist.jsx, etc."""
        
        places_data = [
            # ========== PUDUKKOTTAI PLACES (District ID: 1) ==========
            {
                "district_id": 1,
                "name": "Kundandarkovil",
                "location": "Pudukkottai, Tamil Nadu",
                "tagline": "A masterpiece of Chola architecture",
                "hero_image": "https://jeiwwgoxuldwoxurkalo.supabase.co/storage/v1/object/sign/tnvista/pudukkottai/kundandarkovil/kunext2.jpg",
                "gallery_images": [
                    "https://jeiwwgoxuldwoxurkalo.supabase.co/storage/v1/object/sign/tnvista/pudukkottai/kundandarkovil/kunint4.jpg",
                    "https://jeiwwgoxuldwoxurkalo.supabase.co/storage/v1/object/sign/tnvista/pudukkottai/kundandarkovil/kunint4.jpg"
                ],
                "history": "Kundandarkovil Temple is an ancient rock-cut Shiva temple dating back to the 8th century CE during the Pallava–Muttaraiyar period. Dedicated to Parvathagiriswarar, the Lord of the Hill, this temple is renowned for its early Chola architectural elements and sacred inscriptions.",
                "deity": "Lord Shiva (Parvathagiriswarar)",
                "timings": "6:00 AM – 12:30 PM | 4:00 PM – 8:00 PM",
                "best_month": "December – February",
                "festivals": ["Pradosham", "Maha Shivaratri", "Karthigai Deepam"],
                "reach": "20 km from Pudukkottai town. Accessible via buses, taxis, and private vehicles.",
                "architecture": "The temple showcases early Chola rock-cut architecture with granite carvings, sculpted pillars, and sacred mandapams.",
                "is_featured": True
            },
            {
                "district_id": 1,
                "name": "Palace",
                "location": "Pudukkottai, Tamil Nadu",
                "tagline": "Royal heritage of Pudukkottai",
                "hero_image": "https://jeiwwgoxuldwoxurkalo.supabase.co/storage/v1/object/sign/tnvista/pudukkottai/collector-office/palace2.jpg",
                "gallery_images": [],
                "history": "The Pudukkottai Palace represents the royal heritage of the region.",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": True
            },
            {
                "district_id": 1,
                "name": "Thirumayam Fort",
                "location": "Pudukkottai, Tamil Nadu",
                "tagline": "A fort carved from a single rock",
                "hero_image": "https://jeiwwgoxuldwoxurkalo.supabase.co/storage/v1/object/sign/tnvista/pudukkottai/thirumayam/trmfort.jpg",
                "gallery_images": [],
                "history": "Thirumayam Fort is a historic fort with rock-cut temples.",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": True
            },
            {
                "district_id": 1,
                "name": "Sittanavasal Cave",
                "location": "Pudukkottai, Tamil Nadu",
                "tagline": "Ancient Jain paintings & caves",
                "hero_image": "https://jeiwwgoxuldwoxurkalo.supabase.co/storage/v1/object/sign/tnvista/pudukkottai/sithanavasal/sovextmain.png",
                "gallery_images": [],
                "history": "Sittanavasal is a Jain cave complex with ancient paintings.",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": True
            },
            {
                "district_id": 1,
                "name": "Museum",
                "location": "Pudukkottai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://jeiwwgoxuldwoxurkalo.supabase.co/storage/v1/object/sign/tnvista/pudukkottai/museum/museumin2.jpg",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            },
            {
                "district_id": 1,
                "name": "Viralimalai",
                "location": "Pudukkottai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://jeiwwgoxuldwoxurkalo.supabase.co/storage/v1/object/sign/tnvista/pudukkottai/viralimalai/vrmext1.jpg",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            },
            
            # ========== MADURAI PLACES (District ID: 2) ==========
            {
                "district_id": 2,
                "name": "Meenakshi Amman Temple",
                "location": "Madurai, Tamil Nadu",
                "tagline": "The city's primary attraction, dedicated to Goddess Meenakshi",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Meenachiamman-temple/meenachiamman6.jpg",
                "gallery_images": [],
                "history": "Meenakshi Amman Temple is a historic Hindu temple located on the southern bank of the Vaigai River.",
                "deity": "Goddess Meenakshi and Lord Sundareswarar",
                "timings": "5:00 AM - 12:30 PM, 4:00 PM - 9:30 PM",
                "best_month": "Throughout year",
                "festivals": ["Meenakshi Thirukalyanam", "Chithirai Festival"],
                "reach": "Located in the heart of Madurai city",
                "architecture": "Dravidian architecture with 14 gopurams",
                "is_featured": True
            },
            {
                "district_id": 2,
                "name": "Thirumalai Nayakkar Mahal",
                "location": "Madurai, Tamil Nadu",
                "tagline": "A 17th-century palace showcasing Dravidian and Rajput architecture",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Thirumalai-Nayak-Palace/thirumalainayak5.jpg",
                "gallery_images": [],
                "history": "Built in 1636 by King Thirumalai Nayak",
                "deity": "",
                "timings": "9:00 AM - 5:00 PM",
                "best_month": "October-March",
                "festivals": [],
                "reach": "2 km from Meenakshi Temple",
                "architecture": "Indo-Saracenic style",
                "is_featured": True
            },
            {
                "district_id": 2,
                "name": "Pazhamudhir Solai",
                "location": "Madurai, Tamil Nadu",
                "tagline": "A significant Murugan temple located on a hill",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Pazhamudircholai/pazhamudircholai1.png",
                "gallery_images": [],
                "history": "",
                "deity": "Lord Murugan",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": True
            },
            {
                "district_id": 2,
                "name": "Alagar Koil Temple and Shrine",
                "location": "Madurai, Tamil Nadu",
                "tagline": "A Vishnu temple set at the foot of hills",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Kallazhagar-Sundararaja-Perumal-Temple/azhagar8.png",
                "gallery_images": [],
                "history": "",
                "deity": "Lord Vishnu",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": True
            },
            {
                "district_id": 2,
                "name": "Vandiyur Mariamman Theppakulam",
                "location": "Madurai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Vandiyur-Mariamman-Teppakulam/theppakulam3.jpg",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            },
            {
                "district_id": 2,
                "name": "Gandhi Memorial Museum",
                "location": "Madurai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Gandhi-Memorial-Museum/gmuseum4.png",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            },
            {
                "district_id": 2,
                "name": "Athisayam",
                "location": "Madurai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Athisayam/athisayam1.png",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            },
            {
                "district_id": 2,
                "name": "Samanar Hill",
                "location": "Madurai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/SamanarHill/samanarhill2.png",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            },
            {
                "district_id": 2,
                "name": "Rajaji Park",
                "location": "Madurai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Rajaji-Park/rajajipark1.png",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            },
            {
                "district_id": 2,
                "name": "Tirupparankundram Temple",
                "location": "Madurai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Tirupparankundram/tirupparankundram1.png",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            },
            {
                "district_id": 2,
                "name": "Vaigaidam",
                "location": "Madurai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Vaigaidam/vaigai3.png",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            },
            {
                "district_id": 2,
                "name": "Mary Cathedral",
                "location": "Madurai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Mary-Cathedral/marychurch11.png",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            },
            {
                "district_id": 2,
                "name": "Kazimar Big Mosque",
                "location": "Madurai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Kazimar-Big-Mosque/Kazimar1.webp",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            },
            {
                "district_id": 2,
                "name": "Yanai Malai Hill",
                "location": "Madurai, Tamil Nadu",
                "tagline": "",
                "hero_image": "https://ricowdhzntqrkvnjulox.supabase.co/storage/v1/object/public/tnvista2025allphotos/madurai/Yanai-Malai-Hill/yanaimalai1.png",
                "gallery_images": [],
                "history": "",
                "deity": "",
                "timings": "",
                "best_month": "",
                "festivals": [],
                "reach": "",
                "architecture": "",
                "is_featured": False
            }
        ]
        
        self.stdout.write("📥 Importing places...")
        
        place_count = 0
        for place_data in places_data:
            try:
                # Get the district
                district = District.objects.get(id=place_data['district_id'])
                
                # Create or update place
                place, created = Place.objects.update_or_create(
                    name=place_data['name'],
                    district=district,
                    defaults={
                        'location': place_data['location'],
                        'tagline': place_data['tagline'],
                        'hero_image': place_data['hero_image'],
                        'gallery_images': place_data['gallery_images'],
                        'history': place_data['history'],
                        'deity': place_data['deity'],
                        'timings': place_data['timings'],
                        'best_month': place_data['best_month'],
                        'festivals': place_data['festivals'],
                        'reach': place_data['reach'],
                        'architecture': place_data['architecture'],
                        'is_featured': place_data['is_featured']
                    }
                )
                
                if created:
                    self.stdout.write(f"  ✅ Created: {place.name} in {district.name}")
                else:
                    self.stdout.write(f"  🔄 Updated: {place.name} in {district.name}")
                
                place_count += 1
                
            except District.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"  ❌ District ID {place_data['district_id']} not found for {place_data['name']}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  ❌ Error importing {place_data['name']}: {str(e)}"))
        
        self.stdout.write(self.style.SUCCESS(f"✅ {place_count} places imported successfully!"))