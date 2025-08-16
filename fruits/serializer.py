from rest_framework import serializers
from fruits.models import Fruit


class FruitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fruit
        fields = ['id', 'name', 'image', 'description']