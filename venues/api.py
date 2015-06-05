from rest_framework import routers, serializers, viewsets, mixins
from django.contrib.gis.geos import Point
from munigeo.api import GeoModelSerializer, GeoModelAPIView
from .models import *
import rest_framework_filters as filters


class VenueSerializer(GeoModelSerializer):

    def to_representation(self, obj):
        ret = super(VenueSerializer, self).to_representation(obj)
        if hasattr(obj, 'distance') and obj.distance:
            ret['distance'] = obj.distance.m
        return ret

    class Meta:
        model = Venue
        exclude = ('piste_json', 'x', 'y')


class VenueFilterSet(filters.FilterSet):
    type = filters.NumberFilter()

    class Meta:
        model = Venue
        fields = ['type']


class VenueViewSet(viewsets.ReadOnlyModelViewSet, GeoModelAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    #filter_class = VenueFilterSet

    def get_queryset(self):
        queryset = super(VenueViewSet, self).get_queryset()
        params = self.request.QUERY_PARAMS
        if 'lat' in params and 'lon' in params:
            try:
                lat = float(params['lat'])
                lon = float(params['lon'])
            except ValueError:
                raise ParseError("'lat' and 'lon' need to be floating point numbers")
            point = Point(lon, lat, srid=4326)
            queryset = queryset.distance(point)

            if 'distance' in params:
                try:
                    distance = float(params['distance'])
                    if not distance > 0:
                        raise ValueError()
                except ValueError:
                    raise ParseError("'distance' needs to be a floating point number")
                queryset = queryset.filter(wkb_geometry__distance_lte=(point, distance))
            queryset = queryset.distance(point).order_by('distance')

        if 'type' in params:
            types = params['type'].split(',')
            queryset = queryset.filter(type__in=types)

        return queryset

router = routers.DefaultRouter()
router.register(r'venue', VenueViewSet)
