from django.shortcuts import render
from django.http import HttpResponse
from .models import Mobil

# Create your views here.
def index(request):
	mobils = Mobil.objects.all()
	return render(request, 'mobils/index.html', {'mobils': mobils})


	# output = ', '.join(str(mobil) for mobil in mobils)
	# return HttpResponse(output)