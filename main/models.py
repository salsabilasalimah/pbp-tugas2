# main/models.py

from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.IntegerField()  
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField()
    stock = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name

    def add_stock(self, quantity):
        if quantity > 0:
            self.stock += quantity
            self.save()

    def reduce_stock(self, quantity):
        if 0 < quantity <= self.stock:
            self.stock -= quantity
            self.save()