from django.contrib import admin
from .models import OrderStatus, Orders
# Register your models here.

@admin.register(OrderStatus)
class OrderAdmin(admin.ModelAdmin):
    fields = ('__all__',)
    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            q = ( qs.filter(order_id__delivery_to='DS', order_id__urgent=True)
            .filter(order_id__person_id__kind='C')
            .filter(order_id__person_id__ranks__ranks='P')
            .filter(status='R')
            )
            return q