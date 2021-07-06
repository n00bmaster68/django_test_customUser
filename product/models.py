from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=10, blank=True)
	quantity = models.IntegerField()

	def __str__(self):
		return self.name