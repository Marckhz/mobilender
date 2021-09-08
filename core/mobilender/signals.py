from django.core.exceptions import ValidationError
from .models import OrderStatus, Orders, OrdersDelivered, OrdersFullFilled, OrdersRecieved, Person
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=OrderStatus)
def create_order_delivered(sender, instance, created, **kwargs):
    if created:
        status = instance.status == 'S'
        order_id = instance.order_id
        if status:
            # at this point we assume Order Exist
            obj = OrdersDelivered.objects.get(order_id=order_id)
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
        try:
            order = Orders.objects.get(id=instance.id)
            person = Person.objects.get(id=instance.person_id.id)
            OrdersRecieved.objects.create(order_id=order, person_id=person)
        except (Orders.DoesNotExist, Person.DoesNotExist):
            raise 'Error on Order'

@receiver(post_save,sender=Orders)
def create_order_status(sender, instance, created, **kwargs):
    if created:
        try:
            order = Orders.objects.get(id=instance.id)
            OrderStatus.objects.create(order_id=order)
        except Orders.DoesNotExist:
            raise 'Error'

@receiver(post_save, sender=OrdersRecieved)
def update_order_full_filled(sender, instance, created, **kwargs):
    if created:
        try:  
            order = Orders.objects.get(id=instance.id)
            if not instance.status:
                OrdersFullFilled.objects.create(order_id=order)
            else:
                of = OrdersFullFilled.objects.get(order_id=order)
                of.status = True
                of.save()
        except OrdersFullFilled.DoesNotExist:
            raise 'Error on Order'