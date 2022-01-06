from django.contrib import admin
from .models import School


class SchoolsAdmin(admin.ModelAdmin):
	list_display = ("institute", "building", "courses", "latitude", "longitude","altitude","code", "street", "ownership")
admin.site.register(School, SchoolsAdmin)

