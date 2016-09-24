from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Venues

class VenuesSerializer(serializers.Serializer):

    id = serializers.CharField(required=True, max_length=50)
    name = serializers.CharField(required=True, max_length=100)
    contact = serializers.CharField(required=True)
    location = serializers.CharField(required=True, max_length=250)
    categories = serializers.CharField(required=True)
    distance = serializers.IntegerField(required=True)
    verified = serializers.BooleanField(required=True)
    stats = serializers.CharField(required=True)
    url = serializers.CharField(required=True, max_length=100)
    hours = serializers.CharField(required=False)
    menu = serializers.CharField(required=False)

    # created = serializers.DateTimeField()

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.id = attrs.get('id', instance.id)
            instance.name = attrs.get('name', instance.name)
            instance.contact = attrs.get('contact', instance.contact)
            instance.location = attrs.get('location', instance.location)
            instance.categories = attrs.get('categories', instance.categories)
            instance.distance = attrs.get('distance', instance.distance)
            instance.verified = attrs.get('verified', instance.verified)
            instance.stats = attrs.get('stats', instance.stats)
            instance.url = attrs.get('url', instance.url)
            instance.hours = attrs.get('hours', instance.hours)
            instance.menu = attrs.get('menu', instance.menu)
            return instance

        return Venues(attrs.get('id'),
                      attrs.get('name'),
                      attrs.get('contact'),
                      attrs.get('location'),
                      attrs.get('categories'),
                      attrs.get('distance'),
                      attrs.get('verified'),
                      attrs.get('stats'),
                      attrs.get('url'),
                      attrs.get('hours'),
                      attrs.get('menu'))

    class Meta:
        # model = Venues
        # fields = ('id', 'name', 'address', 'categories', 'distance')
        ordering = ('-distance',)