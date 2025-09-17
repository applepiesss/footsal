import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    CATEGORY_CHOICES = [
        ('footwear', 'Footwear'),
        ('equipment', 'Equipment'),
        ('apparel', 'Apparel'),
    ]

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    is_featured = models.BooleanField()
    brand = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    