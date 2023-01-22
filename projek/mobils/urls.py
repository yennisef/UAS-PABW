from . import views
from django.urls import path

app_name = 'mobils'

urlpatterns = [
    path("", views.index, name='index'),
]
