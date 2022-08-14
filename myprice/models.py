from django.db import models

# Create your models here.

class Uploadss(models.Model):
	upload_image = models.ImageField(null=True, blank=True, upload_to="images/")
	def __int__(self):
		return self.id