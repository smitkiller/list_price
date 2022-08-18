from django.shortcuts import render
import cv2
import os
from django.http import HttpResponseRedirect
from django.conf import settings
from .colordescriptor import ColorDescriptor
from .searcher import Searcher
from .forms import UploadForm
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import csv

@csrf_exempt
def update(request,id_update):
	csv_file = settings.MEDIA_ROOT + '/' + 'index.csv'
	df = pd.read_csv(csv_file, header=None)
	old_name = df.loc[int(id_update)-1, 1]
	if request.method == 'POST':
		df.loc[int(id_update)-1, 1] = request.POST['name']
		df.to_csv(csv_file, header=None, index=False)
		return HttpResponseRedirect('/data')
	return render(request, 'update.html',{'old_name':old_name})

def home(request):
	return render(request, 'home.html',{})

def data(request):
	infor = []
	if os.path.isfile(settings.MEDIA_ROOT + '/' + 'index.csv'):
		csv_file = settings.MEDIA_ROOT + '/' + 'index.csv'
		rf = csv.reader(open(csv_file))
		for d in rf:
			infor.append({'id':d[0],'name':d[1]})

	
	return render(request, 'data.html',{'infor':infor})

def count_row():
	count = 0
	csv_file = settings.MEDIA_ROOT + '/' + 'index.csv'
	if os.path.isfile(csv_file):
		rf = csv.reader(open(csv_file))
		for r in rf:
			count += 1
	return count

@csrf_exempt
def upload(request):
	final_img = []
	submitted = False
	results = []
	name_img = ''
	redirect = False
	csv_file = settings.MEDIA_ROOT + '/' + 'index.csv'
	# csv_file = settings.MEDIA_ROOT + '\\' + 'index.csv'
	cd = ColorDescriptor((8, 12, 3))
	id_ = count_row()
	id_ = id_ + 1
	if request.method == 'POST' and request.FILES:
		form = UploadForm(request.POST, request.FILES)
		name_img = request.FILES['upload_image']
		img_file = settings.IMAGE_ROOT + '/' + str(name_img)
		# img_file = settings.IMAGE_ROOT + '\\' + str(request.FILES['upload_image'])	
		# csv_file = settings.MEDIA_ROOT + '\\' + 'index.csv'
		if form.is_valid():
			form.save()
			# return HttpResponseRedirect('/upload?submitted=True')		
			submitted = True

	else:
		form = UploadForm
		# if 'submitted' in request.GET:
		# 	submitted = True

	if submitted:

		if request.POST['action'] == 'ADD_DATA':
			with open(csv_file, 'a') as f:
				image = cv2.imread(img_file)
				features_add = cd.describe(image)
				features_add = [str(f) for f in features_add]
				f.write("%d,%s,%s\n" % (int(id_),name_img, ",".join(features_add)))
				f.close()
				redirect = True	
		else:
			sch = Searcher(csv_file)
			query = cv2.imread(img_file)
			features = cd.describe(query)
			results = sch.search(features)
			# print(results)
			for (score, path) in results:
				# image_directory = path[:path.rfind('.')]
				full_name = path[:path.rfind('.')]
				# full_name = image_directory.split('\\')[1]
				name = full_name.split('_')[0]
				capacity = full_name.split('_')[1]
				cost = full_name.split('_')[2]
				final_img.append({'score':score,'name':name, 'cost':cost, 'capacity':capacity})
			# print(final_img)

		if os.path.isfile(img_file):
	  		os.remove(img_file)

	if redirect:
	  	return HttpResponseRedirect('/data')
	else:
		return render(request, 'upload.html',{'form':form, 'submitted':submitted, 'data':final_img})