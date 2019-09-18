from django.db import models

# Create your models here.

class Comment(models.Model):
	username = models.TextField(max_length=10)
	comment = models.TextField(max_length=160)
	timestamp=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username