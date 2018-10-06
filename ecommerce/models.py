from django.db import models

"""
Rendering a product for sale
"""
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='img')
    
    def __str__(self):
        return self.name