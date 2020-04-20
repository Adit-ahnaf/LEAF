from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=60)
	description = models.TextField()
	Image = models.FileField()


	def __str__(self):
		return f"{self.title} to {self.description} to {self.Image}"