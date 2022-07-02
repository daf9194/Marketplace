from django.db import models

class Store(models.Model):
    store_name = models.CharField(max_length=50)

    def __str__(self):
        return self.store_name

class Good(models.Model):
    good_name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    store = models.ManyToManyField(Store, related_name='eng')
    pop = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return self.good_name

class GoodBasket(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

