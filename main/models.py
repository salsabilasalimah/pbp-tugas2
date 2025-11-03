# main/models.py
import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('accessories', 'Accessories'),
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu'),
        ('bola', 'Bola'),
        ('kaos kaki', 'Kaos kaki')
    ]


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()  
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=0)
    stock = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

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

    def increment_views(self):
        self.views += 1
        self.save()