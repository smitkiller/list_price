from django.db import models

# Create your models here.

ACTION_CHOICES = (
	('ADD_DATA', 'add data'),
	('SEARCH', 'search'),
	)

class Uploadss(models.Model):
	upload_image = models.ImageField(null=True, blank=True, upload_to="images/")
	action = models.CharField(max_length=50, choices=ACTION_CHOICES)
	def __int__(self):
		return self.id