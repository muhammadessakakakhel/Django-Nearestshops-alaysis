from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.views import generic 
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
# Create your views here.

longitude = 72.9930
latitude = 33.6425

user_location = Point(longitude, latitude, srid=4326)








class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[:8]
    template_name = 'shops/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latitude'] = latitude
        context['longitude'] = longitude
        return context

# from django.shortcuts import render
# from django.contrib.gis.geos import Point
# from django.views import generic
# from django.contrib.gis.db.models.functions import Distance
# from .models import Shop

# class Home(generic.ListView):
#     model = Shop
#     context_object_name = 'shops'
#     template_name = 'shops/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # Get user's location from the query parameters
#         user_latitude = self.request.GET.get('latitude')
#         user_longitude = self.request.GET.get('longitude')

#         # Check if latitude and longitude are provided
#         if user_latitude is not None and user_longitude is not None:
#             # Create a Point object for the user's location
#             user_location = Point(float(user_longitude), float(user_latitude), srid=4326)

#             # Get the nearest 6 shops to the user's location
#             context['shops'] = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[:6]
#         else:
#             # If latitude and longitude are not provided, set shops to an empty list
#             context['shops'] = []

#         return context

