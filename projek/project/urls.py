from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('superuser/', admin.site.urls),
    path("", views.welcome),
    path('mobils/', include('mobils.urls', namespace='mobils')),
    path('readcsv/', include('readcsv.urls', namespace='readcsv')),
    path('readjson/', include('readjson.urls', namespace='readjson')),
    path('readxml/', include('readxml.urls', namespace='readxml'))

    

]



