from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('myprice', include('myprice.urls')),
    path('admin/', admin.site.urls),
]
