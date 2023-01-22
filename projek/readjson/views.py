from django.shortcuts import render
from .rjson import *


# Create your views here.

def index(request):
	return render(request, 'index.html', {'rows':datas})