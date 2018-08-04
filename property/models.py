from django.db import models


# Create your models here.
class Property(models.Model):
    leased = models.BooleanField(default=True)
    residential = 'Residential property'
    commercial = 'Commercial property'
    res_or_com = models.Field.choices(
        (residential, 'Residential property')
        (commercial, 'Commercial property')
    )
    address = models.CharField(max_length=300)
    tenant = models.ForeignObject(parent_link='Tenant')

class Tenant(models.Model):
    f_name = models.CharField()
    l_name = models.CharField()

class LeasePayment(models.Model):
    paid = models.FloatField()
    lease_contract = models.ForeignObject(parent_link='LeaseContract')
    total = lease_contract.rent - paid

class LeaseContract(models.Model):
    agreement_conditions = models.TextField()
    landlord = models.CharField(max_length=300)
    rent = models.FloatField()