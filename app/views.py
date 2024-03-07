from django.shortcuts import render

# Create your views here.
from app.serializers import *
from rest_framework.viewsets import ModelViewSet

class ProductCrud(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductModelSerializer