import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    CATEGORY_CHOICES = [
        ('footwear', 'Footwear'),
        ('equipment', 'Equipment'),
        ('apparel', 'Apparel'),
    ]

    name = models.CharField(max_length=50)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='footwear')
    is_featured = models.BooleanField()
    brand = models.CharField(max_length=20)
    discount = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    @property
    def price_after_disc(self): 
        if self.discount > 0:
            return self.price * (100 - self.discount) / 100
        else:
            return self.price
    
    @property
    def formatted_price(self):
        return f"{int(self.price):,}".replace(',', '.')
    
    @property
    def formatted_price_after_disc(self):
        return f"{int(self.price_after_disc):,}".replace(',', '.')