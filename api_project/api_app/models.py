from django.db import models

# Create your models here.

class Product(models.Model):
    name= models.CharField(max_length=222, unique=True)
    description= models.TextField()
    stock=models.IntegerField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name