from django.shortcuts import render
from django.views.generic import TemplateView
import folium
from django.http import HttpResponse
import os
from django.conf import settings

# Analytics + Visualization
# import pandas as pd
# import altair as alt
# import numpy as np
# from vega_datasets import data

# Create your views here.
class IndexView(TemplateView):
    template_name = 'map_app/index.html'

class UnitedStates(TemplateView):
    template_name = 'map_app/US_Heatmap.html'


# def get_georgia(request):
#     # us_accident_data = pd.read_csv("vis2_geodata_4_5_20.csv")
#     counties = alt.topo_feature(data.us_10m.url, 'counties')
#     source = data.unemployment.url

#     map_georgia =(
#         alt.Chart(data = counties)
#         .mark_geoshape(
#             stroke='black',
#             strokeWidth=1
#         ).encode(color = 'rate:Q').transform_lookup(
#         lookup='id',
#         from_=alt.LookupData(source, 'id', ['rate'])
#     )
#         .transform_calculate(state_id = "(datum.id / 1000)|0")
#         .transform_filter((alt.datum.state_id)==13)
#     )     
#     return HttpResponse(map_georgia.to_json(), content_type='application/json')

# def get_georgia_advanced(request):
#     file_path = os.path.join(settings.BASE_DIR, 'map_app/vis2_geodata_4_5_20.csv')
#     us_accident_data = pd.read_csv(file_path)
#     counties = alt.topo_feature(data.us_10m.url, 'counties')

#     alt.data_transformers.disable_max_rows()

#     df2 = us_accident_data[us_accident_data.State=='GA']
#     df3 = df2[df2.Year==2016]
#     df3.reset_index(inplace=True)

#     map_georgia2 = (
#         alt.Chart(data = counties)
#         .mark_geoshape(
#             stroke='black',
#             strokeWidth=1,
#             fill=None
#         )
#         .transform_calculate(state_id = "(datum.id / 1000)|0").encode(tooltip=['id:N'])
#         .transform_filter((alt.datum.state_id)==13)
#     )

#     points_2016 = alt.Chart(df3).mark_point().encode(
#     latitude='Start_Lat',
#     longitude='Start_Lng',
#     color='Severity:N',
#     tooltip=['County:N','Geo_ID:N','City:N','Year:N','Severity:N','Start_Time:O']
#     )

#     # georgia_advanced = (points_2016 + map_georgia2).properties(width = 800, height = 800)
#     decauter = alt.Chart(counties).mark_geoshape(
#         stroke='black',
#         strokeWidth=1,
#         fill='yellow'
#     ).transform_filter((alt.datum.id == 13087))

#     coweta = alt.Chart(counties).mark_geoshape(
#             stroke='black',
#             strokeWidth=1,
#             fill='yellow'
#         ).transform_filter((alt.datum.id == 13077))

#     dodge = alt.Chart(counties).mark_geoshape(
#             stroke='black',
#             strokeWidth=1,
#             fill='yellow'
#         ).transform_filter((alt.datum.id == 13091))

#     franklin = alt.Chart(counties).mark_geoshape(
#             stroke='black',
#             strokeWidth=1,
#             fill='yellow'
#         ).transform_filter((alt.datum.id == 13149))

#     murray = alt.Chart(counties).mark_geoshape(
#             stroke='black',
#             strokeWidth=1,
#             fill='yellow'
#         ).transform_filter((alt.datum.id == 13213))

#     (decauter + coweta + dodge + franklin + murray + points_2016 + map_georgia2).properties(width = 1000, height = 1000) 
#     georgia_advanced = (decauter + coweta + dodge + franklin + murray + points_2016 + map_georgia2)
#     return HttpResponse(georgia_advanced.to_json(), content_type='application/json')


# def get_arkansas(request):
#     # us_accident_data = pd.read_csv("vis2_geodata_4_5_20.csv")
#     counties = alt.topo_feature(data.us_10m.url, 'counties')
#     source = data.unemployment.url

#     map_arkansas =(
#         alt.Chart(data = counties)
#         .mark_geoshape(
#             stroke='black',
#             strokeWidth=1
#         ).encode(color = 'rate:Q').transform_lookup(
#         lookup='id',
#         from_=alt.LookupData(source, 'id', ['rate'])
#     )
#         .transform_calculate(state_id = "(datum.id / 1000)|0")
#         .transform_filter((alt.datum.state_id)==5)
#     )    
#     return HttpResponse(map_arkansas.to_json(), content_type='application/json')

# def get_kansas(request):
#     # us_accident_data = pd.read_csv("vis2_geodata_4_5_20.csv")
#     counties = alt.topo_feature(data.us_10m.url, 'counties')
#     source = data.unemployment.url

#     map_kansas =(
#         alt.Chart(data = counties)
#         .mark_geoshape(
#             stroke='black',
#             strokeWidth=1
#         ).encode(color = 'rate:Q').transform_lookup(
#         lookup='id',
#         from_=alt.LookupData(source, 'id', ['rate'])
#     )
#         .transform_calculate(state_id = "(datum.id / 1000)|0")
#         .transform_filter((alt.datum.state_id)==20)
#     )   
#     return HttpResponse(map_kansas.to_json(), content_type='application/json')
