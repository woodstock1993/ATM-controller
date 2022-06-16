from django.db import models


class Card(models.Model):
    card_number = models.CharField(max_length=256, null=False, blank=False, primary_key=True)
    pin_number = models.CharField(max_length=256, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey('atm.Account', on_delete=models.CASCADE)



class Account(models.Model):
    account_number = models.CharField(max_length=256, null=False, blank=False, primary_key=True)
    balance = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
