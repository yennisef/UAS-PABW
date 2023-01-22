from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    price = models.CharField(max_length=60)
    def __str__(self):
        return self.name