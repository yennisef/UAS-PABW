from . import views
from django.urls import path

app_name = 'readxml'

urlpatterns = [
    path("", views.index, name='index'),
]
