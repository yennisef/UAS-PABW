from rest_framework import viewsets

from .serializers import CarsSerializer
from .models import Cars


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
