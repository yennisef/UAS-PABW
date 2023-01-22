from django.db import models

# Create your models here.
class Mobil(models.Model):
	brand = models.CharField(max_length=150)
	model = models.CharField(max_length=150)
	price = models.IntegerField()

	def __str__(self):
		return self.brand