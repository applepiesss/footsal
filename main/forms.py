from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "brand", "price", "discount", "stock", "thumbnail", "category", "description", "is_featured"]