from django import forms
from django.forms import ModelForm
from .models import Uploadss, FeaturesImg

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
			# 'features' : forms.Textarea(attrs={'class':'form-control', 'cols': 80, 'rows': 20}),
		}


class FeaturesForm(ModelForm):
	class Meta:
		model = FeaturesImg
		# fields = ('upload_image',)
		fields = ('name',)

		labels = {
			'name' : '',
		}

		widgets = {
			'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
			# 'features' : forms.Textarea(attrs={'class':'form-control', 'cols': 80, 'rows': 20}),
		}