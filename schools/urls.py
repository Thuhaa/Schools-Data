from django.urls import path
from . import views

urlpatterns = [
path('', views.homepage_view, name="home"),
path('geojson/', views.geojson_view, name="geojson-view")
]