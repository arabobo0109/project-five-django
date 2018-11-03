from django.db import models

"""
Rendering a product for sale
"""
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    strap = models.CharField(max_length=254, default='')
    description = models.TextField(default='')
    upvotes = models.IntegerField(default='0')
    tag = models.CharField(max_length=30, blank=True, null=True, default='')
    target = models.DecimalField(max_digits=6, decimal_places=2, default='0.00')
    remaining = models.DecimalField(max_digits=6, decimal_places=2, default='0.00')
    tribute = models.DecimalField(max_digits=6, decimal_places=2, default='0.00')
    image = models.ImageField(upload_to="img", blank=True, null=True, default='')
    status_choices = (
        ('PR', 'In Progress'),
        ('PL', 'In Planning'),
        ('C', 'Completed'),
        ('W', 'Waiting to be Funded'),
    )
    status = models.CharField(max_length=2, choices=status_choices, default='W')
    def __str__(self):
        return self.name