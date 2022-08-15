from django.shortcuts import render
from django.template import RequestContext
# import cv2
import os
from django.http import HttpResponseRedirect
from django.conf import settings
# from .colordescriptor import ColorDescriptor
# from .searcher import Searcher
from .forms import UploadForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
	final_img = []
	submitted = False
	results = []
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		# # img_file = settings.IMAGE_ROOT + '\\' + str(request.FILES['upload_image'])
		# # csv_file = settings.MEDIA_ROOT + '\\' + 'index.csv'
		if form.is_valid():
			return HttpResponseRedirect('/?submitted=True')
			# submitted = True
		# 	# form.save()
		# 	# cd = ColorDescriptor((8, 12, 3))
		# 	# sch = Searcher(csv_file)
		# 	# query = cv2.imread(img_file)
		# 	# features = cd.describe(query)
		# 	# results = sch.search(features)
		# 	# # print(results)
		# 	# for ((score, cost), resultID) in results:
		# 	# 	final_img.append({'score':score, 'cost':cost, 'path':resultID})
		# 	# # print(final_img)
		# 	submitted = True

			# if os.path.isfile(img_file):
  	# 			os.remove(img_file)
	else:
		form = UploadForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'home.html',{'form':form, 'submitted':submitted, 'data':final_img})