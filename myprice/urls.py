from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('upload', views.upload, name='upload-img'),
	path('up_success', views.up_success, name='upload-success'),
	path('data', views.data, name='data-img'),
	path('delete/<id_del>', views.delete, name='del-data'),
	path('update/<id_update>', views.update, name='update-name'),
]