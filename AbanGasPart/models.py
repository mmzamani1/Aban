from django.db import models


class Item(models.Model):
    CATEGORIES = [
        ('گازی', 'Gas'),
        ('برقی', 'Electric'),
    ]
    CATEGOTY_LIST = ['برقی', 'گازی']
    title = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='media/', default='media/products/default.png', blank=True)
    catalog = models.ImageField(upload_to='media/', default='media/catalogs/default.png', blank=True)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.title}'
    
    
    
    
