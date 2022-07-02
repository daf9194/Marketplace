from django.db import models
from django.contrib.auth.models import User
from app_goods.models import Good, GoodBasket

class Profile(models.Model):

    STATUS = [
        ('JUN', 'jun'),
        ('MDL', 'mdl'),
        ('SEN', 'sen')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0, blank=True)
    status = models.CharField(max_length=3,choices=STATUS, default='JUN', blank=True)
    basket = models.ManyToManyField(GoodBasket, blank=True)
    total_buy = models.PositiveIntegerField(default=0, blank=True)