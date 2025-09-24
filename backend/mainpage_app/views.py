import json
from django.core import serializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ItemUnits, ItemUnitsSerializer
from rest_framework.generics import ListAPIView, CreateAPIView

class ItemUnitsListView(ListAPIView):
    queryset = ItemUnits.objects.all()
    serializer_class = ItemUnitsSerializer


class ItemUnitsCreateView(CreateAPIView):
    queryset = ItemUnits.objects.all()  # Not strictly needed, but useful for validation
    serializer_class = ItemUnitsSerializer  # The serializer that handles creation


# Create your views here.
@api_view(['GET','POST'])
def getItemUnits(request):
	data = serializers.serialize("json", ItemUnits.objects.all())
	print(data)
	return Response(data)

