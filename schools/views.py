import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import School
from .utils import get_geojson

def homepage_view(request):
	data = json.dumps(get_geojson())
	context = {"data":data}
	return render(request, "schools/index.html", context)

def geojson_view(request):
	geojson = get_geojson()
	return JsonResponse(geojson)
