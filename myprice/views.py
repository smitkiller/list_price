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


def delete(request,id_del):
	csv_file = settings.MEDIA_ROOT + '/' + 'index.csv'
	if os.path.isfile(csv_file):
		# df = pd.read_csv(csv_file, header=None)
		# df.drop(int(id_del)-1,axis=0,inplace=True)
		# df.to_csv(csv_file, header=None, index=False)
		df = pd.read_csv(csv_file, header=None)
		df.loc[int(id_del)-1, 1] = ''
		df.to_csv(csv_file, header=None, index=False)
	return HttpResponseRedirect('/data')

@csrf_exempt
def update(request,id_update):
	csv_file = settings.MEDIA_ROOT + '/' + 'index.csv'
	if os.path.isfile(csv_file):
		df = pd.read_csv(csv_file, header=None)
		old_name = df.loc[int(id_update)-1, 1]
		if request.method == 'POST':
			df.loc[int(id_update)-1, 1] = request.POST['name']
			df.to_csv(csv_file, header=None, index=False)
			return HttpResponseRedirect('/data')
	return render(request, 'update.html',{'old_name':old_name})

def home(request):
	count = count_row()
	return render(request, 'home.html',{'count':count})

def data(request):
	infor = []
	csv_file = settings.MEDIA_ROOT + '/' + 'index.csv'
	if os.path.isfile(csv_file):	
		rf = csv.reader(open(csv_file))
		for d in rf:
			if d[1] != '':
				infor.append({'id':d[0],'name':d[1]})
	return render(request, 'data.html',{'infor':infor})

def count_row():
	last_id = 0
	csv_file = settings.MEDIA_ROOT + '/' + 'index.csv'
	if os.path.isfile(csv_file):
		rf = csv.reader(open(csv_file))
		for r in rf:
			if int(r[0]) > int(last_id):
				last_id = r[0]
	return int(last_id)

@csrf_exempt
def upload(request):
	final_img = []
	submitted = False
	action = False
	results = []
	name_img = ''
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
			# submitted = True

	if submitted:

		if request.POST['action'] == 'ADD_DATA':
			action = True
			with open(csv_file, 'a') as f:
				image = cv2.imread(img_file)
				features_add = cd.describe(image)
				features_add = [str(f) for f in features_add]
				f.write("%d,%s,%s\n" % (int(id_),request.POST['file_name'], ",".join(features_add)))
				f.close()		
		else:
			sch = Searcher(csv_file)
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