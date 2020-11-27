from django.db import models


class Transaction(models.Model):
    authority = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=200, blank=False, null=False)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    amount = models.IntegerField(blank=False, null=False)
    reference_id = models.IntegerField(blank=True, null=True)
    