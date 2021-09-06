from .models import OrderStatus, Orders, OrdersDelivered, OrdersFullFilled, OrdersRecieved
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=OrderStatus)
def create_order_delivered(sender, instance, created, **kwargs):
    if created:
        status = sender.status == 'S'
        order_id = OrderStatus.order_id
        if status:
            # at this point we assume Order Exist
            obj = OrdersDelivered.object.get(order_id=order_id)
            obj.status = True
            obj.save()
        else:
            try:
                obj = OrdersDelivered.objects.get(order_id=order_id)
            except OrdersDelivered.DoesNotExist:
                OrdersDelivered.objects.create(order_id=order_id)

@receiver(post_save, sender=Orders)
def create_order_recieved(sender, instance, created, **kwargs):
    if created:
        order_id = sender.id
        person_id = sender.person_id
        OrdersRecieved.objects.create(order_id=order_id, person_id=person_id)

@receiver(post_save, sender=OrdersRecieved)
def update_order_full_filled(sender, instance, created, **kwargs):
    if created:
        order_id = sender.order_id
        try:
            obj = OrdersFullFilled.objects.get(order_id=order_id)
            obj.status = True
        except OrdersFullFilled.DoesNotExist:
            raise 'Order not Found'
