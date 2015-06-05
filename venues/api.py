from rest_framework import routers, serializers, viewsets, mixins, filters
from munigeo.api import GeoModelSerializer, GeoModelAPIView
from .models import *
import django_filters


class VenueSerializer(GeoModelSerializer):

    class Meta:
        model = Venue
        exclude = ('piste_json', 'x', 'y')


class VenueViewSet(viewsets.ReadOnlyModelViewSet, GeoModelAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

router = routers.DefaultRouter()
router.register(r'venue', VenueViewSet)
