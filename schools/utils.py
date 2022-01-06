from .models import School
from django.core import serializers
import json


def get_geojson():
	data_json_string = serializers.serialize(
		'json',

		School.objects.all(), 
		fields=(
			"institute", 
			"building", 
			"courses", 
			"latitude", 
			"longitude",
			"altitude",
			"code", 
			"street", 
			"ownership"
			)
		)
	data_list = json.loads(data_json_string)

	geojson_template = {
	"type": "FeatureCollection",
	"features":[]}

	features_list = []

	for entry in data_list:
		features_list.append(
			{
				"type": "Feature",
				"geometry": {
					"type": "Point",
					"coordinates": [entry["fields"]["longitude"], entry["fields"]["latitude"]]
					},
					"properties": 
						{
						"institute": entry["fields"]["institute"],
						"building": entry["fields"]["building"],
						"courses": entry["fields"]["courses"],
						"altitude": entry["fields"]["altitude"],
						"code": entry["fields"]["code"],
						"street": entry["fields"]["street"],
						"ownership": entry["fields"]["ownership"]
						}
			}
		)

	geojson_template = {
	"type": "FeatureCollection",
	"features":features_list
	}
	return geojson_template