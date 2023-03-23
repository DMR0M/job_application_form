from django.db import models


class Form(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(max_length=40)
	date = models.DateField(auto_now_add=True)
	occupation = models.CharField(max_length=40)

	def __str__(self):
		return f"{self.first_name} {self.last_name}'s Form"

