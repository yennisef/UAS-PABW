from . import views
from django.urls import path

app_name = 'readjson'

urlpatterns = [
    path("", views.index, name='index'),
]
