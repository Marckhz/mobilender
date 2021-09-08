from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter
from django.db.models import query
from django_admin_multiple_choice_list_filter.list_filters import MultipleChoiceListFilter
from django.contrib.auth.models import User
from .models import OrderStatus, Orders, UserRanks
# Register your models here.
import ast
from functools import wraps


def person_type(client):
    client = 'Client 'if client == 'C' else 'Vendor'
    return client

class CustomRankFilter(SimpleListFilter):
    title = 'client ranks'
    parameter_name = 'ranks'

    # could use the extensino that is instatled multiple but so little time
    def lookups(self, request, model_admin):
        return [
            ('P', 'Platinum-Urgent'),
            ('N', 'Normal'),
            ('P-!', 'Platinum-Not-Urgent')
        ]

    def __qs(self, queryset, urgent=False):
        return (queryset.filter(order_id__person_id__ranks__ranks='P')
                .filter(order_id__delivery_to='DS')
                .filter(order_id__urgent=urgent)
                .filter(status='R')
            )

    def queryset(self, request, queryset):
        qs = queryset
        condition = self.value()
        if condition  == 'P':
            qs = self.__qs(queryset, urgent=True)
        elif condition == 'P-!':
            qs = self.__qs(queryset)
        return qs

@admin.register(OrderStatus)
class OrderAdmin(admin.ModelAdmin):
    list_filter = (CustomRankFilter,)

    list_display = ['order_id', 
                    'status',
                    'client_type', 
                    'client_rank',
                    'person_id',
                    'delivery_to'
                    ]
    
    @admin.display(ordering='order_id__person_id__kind')
    def client_type(self, obj):
        client_raw = obj.order_id.person_id.kind
        client_dict = ast.literal_eval(client_raw)
        client = client_dict.get('kind')
        client = person_type(client)
        return client
    
    @admin.display(ordering='order_id__person_id__ranks')
    def client_rank(self, obj):
        person = obj.order_id.person_id
        rank = UserRanks.objects.get(person_id=person)
        return rank
    
    @admin.display(ordering='order_id__person_id')
    def person_id(self, obj):
        return obj.order_id.person_id
    
    @admin.display(ordering='order_id__delivery_to')
    def delivery_to(self, obj):
        return obj.order_id.delivery_to

