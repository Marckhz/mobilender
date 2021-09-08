# Create your models here.
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


from django.db import models
import datetime


class Person(models.Model):

    VENDOR = 'V'
    CLIENT = 'C'
    USER_KIND = [
        (VENDOR, 'Vendor'),
        (CLIENT, 'Client'),
    ]

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True, null=False)
    code = models.CharField(max_length=100, unique=True, null=False)
    # a reference to a bucket?
    photo = models.CharField(max_length=50, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    kind = models.CharField(max_length=2, choices=USER_KIND, null=False)

    def __str__(self) -> str:
        return f'{self.name}-{self.id}'


class Address(models.Model):
    street = models.CharField(max_length=50, null=False)
    zipcode = models.CharField(max_length=10, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    person_id = models.ForeignKey(Person,related_name='address', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Address - {self.city, self.state}'

class UserRanks(models.Model):
    
    NORMAL = 'N'
    SILVER = 'S'
    GOLD = 'G'
    PLATINUM = 'P'

    RANKS =[
        (NORMAL, 'Normal'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum')
    ]

    ranks = models.CharField(max_length=1, choices=RANKS)
    person_id = models.ForeignKey(Person, related_name='ranks', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.ranks}'


class Articles(models.Model):
    #Here must be many to many
    code = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=100, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    vendor_id = models.ManyToManyField('mobilender.Person')


    def __str__(self) -> str:
        return f'Article - {self.vendor_id}'


#  class DistributionCenter(models.Model):
#     name = models.CharField(max_length=50, null=False)
#     # address = models.ForeignKey('mobilender.Address', on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return f'Distribution Center - {self.name}'

# class BranchOffice(models.Model):
#     reference = models.CharField(max_length=50, null=False)

#     def __str__(self) -> str:
#         return f'Branch Office - {self.reference}'

# class AssociatedFirm(models.Model):
#     reference = models.CharField(max_length=50, null=False)
#     associated_code = models.CharField(max_length=50, null=False)
#     order_detail = models.TextField(null=False)

#     def __str__(self) -> str:
#         return f'Associated Firm - {self.reference}'



class Sites(models.Model):
    
    DISTRIBUTION_CENTER = 'DS'
    BRANCH_OFFICE = 'BF'
    ASSOCIATED_FIRM = 'AF'
    SITES = [
        (DISTRIBUTION_CENTER, 'Distribution Center'),
        (BRANCH_OFFICE, 'Branch Office'),
        (ASSOCIATED_FIRM, 'Associated Firm')
    ]

    kind = models.CharField(max_length=2, choices=SITES)
    name = models.CharField(max_length=50)
    reference = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'

class Orders(models.Model):

    DISTRIBUTION_CENTER = 'DS'
    BRANCH_OFFICE = 'BF'
    ASSOCIATED_FIRM = 'AF'
    SITES = [
        (DISTRIBUTION_CENTER, 'Distribution Center'),
        (BRANCH_OFFICE, 'Branch Office'),
        (ASSOCIATED_FIRM, 'Associated Firm')
    ]

    person_id = models.ForeignKey('mobilender.Person', on_delete=models.CASCADE)
    on_request_date = models.DateTimeField(auto_now=True)
    on_delivery_date = models.DateTimeField(null=False)
    urgent = models.BooleanField(null=False, default=False)
    article_id = models.ForeignKey('mobilender.Articles', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    delivery_to = models.CharField(max_length=2, choices=SITES)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id= models.PositiveIntegerField()
    # site = content_object = GenericForeignKey('content_type', 'object_id')
    site_id = models.ForeignKey("mobilender.Sites", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id}'

class OrderStatus(models.Model):

    SENT = 'S'
    ON_GOING = 'OG'
    READY = 'R'

    STATUS = [
        (SENT, 'Sent'),
        (ON_GOING, 'On Going'),
        (READY, 'Ready')
    ]
    status = models.CharField(max_length=2, choices=STATUS, default='R')
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'order: {self.order_id}'

class OrdersRecieved(models.Model):
    status = models.BooleanField(default=False)
    person_id = models.ForeignKey('mobilender.Person', on_delete=models.CASCADE)
    order_id = models.ForeignKey('mobilender.Orders', on_delete=models.CASCADE)

class OrdersDelivered(models.Model):
    status = models.BooleanField(default=False)
    order_id = models.ForeignKey('mobilender.Orders', on_delete=models.CASCADE)


class OrdersFullFilled(models.Model):
    status = models.BooleanField(default=False)
    order_id = models.ForeignKey('mobilender.Orders', on_delete=models.CASCADE)

#implement cool signal for this


    

        
        


