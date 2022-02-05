import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import School
from .utils import get_geojson

def homepage_view(request):
	data = json.dumps(get_geojson())
	obj = json.loads(data)
	data_list = obj['features']
	'''for x in data_list:
					institute_list.append(x['properties']['institute'])'''

	context = {"data":data, "data_list":data_list}
	return render(request, "schools/index.html", context)

def geojson_view(request):
	geojson = get_geojson()
	return JsonResponse(geojson)
