from mobilender.models import OrderStatus
from mobilender.models import Sites
from mobilender.models import Orders
from mobilender.models import Articles
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User

from mobilender.models import Person, Address, UserRanks


class RepresentationCustom(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return value.name

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id',
                  'street',
                  'zipcode',
                  'city',
                  'state',
                ]

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRanks
        fields = ['ranks',]


class ClientSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)
    ranks = RankSerializer(many=True)

    class Meta:
        model = Person
        read_only_fields = ['created_on']
        fields = [
                  'name',
                  'code',
                  'photo', 
                  'ranks',
                  'address',
                  'kind',
                  'created_on',
                ]

    def create(self, validated_data):
        try:
            address_data = validated_data.pop('address')
            rank_data = validated_data.pop('ranks')
            address_data = next(iter(address_data))
            rank_data = next(iter(rank_data))
            client = Person.objects.create(**validated_data)
            Address.objects.create(person_id=client, **address_data)
            UserRanks.objects.create(person_id=client, **rank_data)
        except ValidationError:
            raise serializers.ValidationError({"detail": "input is not valid"})
       
        return client


class ArticlesSerializer(serializers.ModelSerializer):
    vendor_id = RepresentationCustom(many=True, queryset=Person.objects.all())
    class Meta:
        model = Articles
        fields = ['code', 'description', 'price', 'vendor_id','id']

class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ['kind', 'name', 'reference', 'code','id']

class OrdersSerializer(serializers.ModelSerializer):
    sites = RepresentationCustom(many=True, queryset=Sites.objects.all() )
    class Meta:
        model = Orders
        fields = ['on_request_date',
                  'on_delivery_date',
                  'urgent',
                  'quantity',
                  'delivery_to',
                  'person_id',
                  'article_id',
                  'sites',
                  'id'
                ]

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['status', 'finished', 'order_id']