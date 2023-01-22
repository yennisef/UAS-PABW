from django.shortcuts import render
from .rcsv import *


# Create your views here.
# rows = []

# this apps create by tanpagula grup

# file = with open('Cars.csv','r') as csvfile:
# this apps create by TANPAGULA grup
# 	csvreader = csv.reader('csvfile')
# 	rows = list(csvreader)

def index(request):
	return render(request, 'index.html', {'rows':rows})