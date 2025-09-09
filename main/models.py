import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('name', 'Name'),
        ('price', 'Price'),
        ('description', 'Description'),
        ('thumbnail', 'Thumbnail'),
        ('category', 'Category'),
        ('is_featured', 'Is_featured'),
        ('brand', 'Brand'),
    ]
    
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    categoty = models.CharField(max_length=20)
    is_featured = models.BooleanField()
    brand = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    