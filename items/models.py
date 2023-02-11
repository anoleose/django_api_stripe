from django.db import models
from django.urls import reverse

class Item(models.Model):
	name        = models.CharField(max_length=200)
	description = models.TextField()
	price       = models.DecimalField(decimal_places=2, max_digits=20)
	created_at  = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True, auto_now_add=False)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("items:detail_item", kwargs={'id':self.id})