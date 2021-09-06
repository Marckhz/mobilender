from api.serializers import OrderStatusSerializer
from mobilender.models import OrderStatus
from api.serializers import OrdersSerializer
from mobilender.models import Orders
from api.serializers import ArticlesSerializer
from mobilender.models import Articles
from api.serializers import ClientSerializer, AddressSerializer
from rest_framework import viewsets


from mobilender.models import Person, Address
# Create your views here.
# must add pagination


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = ClientSerializer

class AddresViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

# class UrgentOrdersViewSet(generics.ListAPIView):
#     serializer_class = OrderStatusSerializer
    
#     def get_queryset(self, request, *args, **kwargs):
#         OrderStatus.objects.filter()



