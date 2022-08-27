from django.shortcuts import render
import cv2
import os
from django.http import HttpResponseRedirect
from django.conf import settings
from .colordescriptor import ColorDescriptor
from .searcher import Searcher
from .forms import UploadForm, FeaturesForm
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import csv
from .models import FeaturesImg


def delete(request,id_del):
	features_img = FeaturesImg.objects.get(pk=id_del)
	features_img.delete()
	return HttpResponseRedirect('/data')

# @csrf_exempt
def update(request,id_update):
	features_img = FeaturesImg.objects.get(pk=id_update)
	form = FeaturesForm(request.POST or None, instance=features_img)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/data')
	return render(request, 'update.html',{'features_img':features_img, 'form':form})

def home(request):
	return render(request, 'home.html',{})

def data(request):
	results = FeaturesImg.objects.all()
	return render(request, 'data.html',{'infor':results})

# @csrf_exempt
def upload(request):
	final_img = []
	submitted = False
	action = False
	results = []
	name_img = ''
	csv_file = settings.MEDIA_ROOT + '/' + 'index.csv'
	cd = ColorDescriptor((8, 12, 3))
	if request.method == 'POST' and request.FILES:
		form = UploadForm(request.POST, request.FILES)
		name_img = request.FILES['upload_image']
		name = request.POST['file_name']
		img_file = settings.IMAGE_ROOT + '/' + str(name_img)
		if form.is_valid():
			form.save()
			# return HttpResponseRedirect('/upload?submitted=True')		
			submitted = True

	else:
		form = UploadForm
		# if 'submitted' in request.GET:
			# submitted = True

	if submitted:

		if request.POST['action'] == 'ADD_DATA':
			action = True
			image = cv2.imread(img_file)
			features_add = cd.describe(image)
			features_add = [str(f) for f in features_add]
			addform = FeaturesImg(name=name,features= ",".join(features_add))
			addform.save()
		else:
			data_list = FeaturesImg.objects.all()
			sch = Searcher(data_list)
			query = cv2.imread(img_file)
			features = cd.describe(query)
			results = sch.search(features)
			# print(results)
			for ((score, id_img), path) in results:
				# image_directory = path[:path.rfind('.')]
				# full_name = path[:path.rfind('.')]
				# full_name = image_directory.split('\\')[1]
				data = path.split('_')
				c = 0
				for d in data:
					c += 1
				if c < 3:
					name = path
					capacity = ''
					cost = ''
				else:
					name = data[0]
					capacity = data[1]
					cost = data[2]
				final_img.append({'score':score, 'id':id_img, 'name':name, 'cost':cost, 'capacity':capacity})
			# print(final_img)

		if os.path.isfile(img_file):
	  		os.remove(img_file)

		
	if action:
		return HttpResponseRedirect('/up_success')
	else:
		return render(request, 'upload.html',{'form':form, 'submitted':submitted, 'data':final_img})



def up_success(request):
	return render(request, 'up_success.html',{})