from rest_framework import serializers

from .models import Cars

class CarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ('name', 'model', 'price')