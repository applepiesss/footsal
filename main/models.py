import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('footwear', 'Footwear'),
        ('equipment', 'Equipment'),
        ('apparel', 'Apparel'),
        ('women', 'Women'),
        ('men', 'Men'),
        ('kids', 'Kids'),
        ('general', 'General')
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
    