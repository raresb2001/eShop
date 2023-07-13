from django.db import models

# Create your models here.

class Products(models.Model):

    product = models.CharField(max_length=100)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} - {self.bought}"

