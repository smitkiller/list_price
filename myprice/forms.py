from django import forms
from django.forms import ModelForm
from .models import Uploadss

class UploadForm(ModelForm):
	class Meta:
		model = Uploadss
		# fields = ('upload_image',)
		fields = '__all__'

		labels = {
			'action' : '',
			'file_name' : '',
			'upload_image' : '',
		}

		widgets = {
			'upload_image' : forms.FileInput(attrs={'class':'form-control'}),
			'action' : forms.Select(attrs={'class':'form-select'}),
			'file_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'File Name'}),
		}