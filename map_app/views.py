from django.shortcuts import render
from django.views.generic import TemplateView
import folium
# import os
# import plotly.figure_factory as ff
# import numpy as np
# import pandas as pd
# import plotly.graph_objs as go
# import plotly.offline as opy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'map_app/index.html'

    def get_context_data(self, **kwargs):

        figure = folium.Figure()

        m = folium.Map(
            location=[39, -98],
            zoom_start=4,
            width=700,
            height=500,
        )
        m.add_to(figure)
        # figure.render()
        style_statement = '<style>element.style{width:50%}</style>'
        m=m.get_root().header.add_child(folium.Element(style_statement))
        html_string = m.get_root().render()
        # m=m._repr_html_()
        return { "map": html_string }
