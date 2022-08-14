from django import forms
from django.forms import ModelForm
from .models import Uploadss

class UploadForm(ModelForm):
	class Meta:
		model = Uploadss
		fields = ('upload_image',)
		# fields = '__all__'
