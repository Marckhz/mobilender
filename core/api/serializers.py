from mobilender.models import OrderStatus
from mobilender.models import Sites
from mobilender.models import Orders
from mobilender.models import Articles
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User

from mobilender.models import Person, Address, UserRanks
import json


class RepresentationCustom(serializers.PrimaryKeyRelatedField):
    def __init__(self, field, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__field = field
    
    def to_representation(self, value):
        field = self.__field
        name = getattr(value, field)  if hasattr(value, field) else value.id   
        return name


    def use_pk_only_optimization(self):
        return False

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
                  'id'
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
    vendor_id = RepresentationCustom(many=True, queryset=Person.objects.all(), field='name')
    class Meta:
        model = Articles
        fields = ['code', 'description', 'price', 'vendor_id','id']


class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ['kind', 'name', 'reference', 'code','id']

class OrdersSerializer(serializers.ModelSerializer):
    
    site_id = RepresentationCustom(many=False, queryset=Sites.objects.all(), field='name' )
    on_delivery_date = serializers.DateField(format=None, input_formats=['%Y-%m-%d'])
    on_request_date = serializers.DateField(format=None, input_formats=['%Y-%m-%d'])
    person_id = RepresentationCustom(many=False, queryset=Person.objects.all(), field='name' )
    article_id = RepresentationCustom(many=False, queryset=Articles.objects.all(), field='code')

    class Meta:
        model = Orders
        fields = ['on_request_date',
                  'on_delivery_date',
                  'urgent',
                  'quantity',
                  'delivery_to',
                  'person_id',
                  'article_id',
                  'site_id',
                  'id'
                ]

    def create(self, validate_data):
        site_id = validate_data.pop('site_id')
        if site_id:
            site_id = site_id
        order = Orders.objects.create(site_id=site_id, **validate_data)
        return order
        
class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['status',  'order_id']

