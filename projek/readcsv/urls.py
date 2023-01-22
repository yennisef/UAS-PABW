from . import views
from django.urls import path

# this apps create by TANPAGULA grup

app_name = 'readcsv'

urlpatterns = [
    path("", views.index, name='index'),
]
