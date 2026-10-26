from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Manufacturer
from .serializers import ManufacturerSerializer

class ManufacturerViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

    @action(methods=['GET'], detail=False, url_path='russian')
    def russian_manufacturer_list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(country='Россия')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)