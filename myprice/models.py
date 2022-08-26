from django.db import models

# Create your models here.

ACTION_CHOICES = (
	('','--- Select Action ---'),
	('ADD_DATA', 'add data'),
	('SEARCH', 'search'),
	)

class Uploadss(models.Model):
	upload_image = models.ImageField(upload_to="images/")
	# upload_image = models.ImageField(null=True, blank=True, upload_to="images/")
	action = models.CharField(max_length=50, choices=ACTION_CHOICES)
	file_name = models.CharField('File Name', max_length=120)
	
	def __str__(self):
		return self.file_name


class FeaturesImg(models.Model):
	name = models.CharField(max_length=120)
	features = models.CharField(max_length=500)

	def __str__(self):
		return self.name
