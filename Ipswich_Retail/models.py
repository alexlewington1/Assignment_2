from django.db import models

# Model creation
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Coming soon...")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/', default='media/default.jpg')

    def __str__(self):
        return self.name
