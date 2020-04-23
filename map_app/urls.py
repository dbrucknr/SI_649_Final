from django.urls import path
from .views import IndexView, UnitedStates#, get_georgia, get_arkansas, get_kansas, get_georgia_advanced
from django.views.generic import TemplateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('map_app/USA.html', TemplateView.as_view(template_name='map_app/USA.html'), name='USA'),
    # path('georgia/', get_georgia, name='georgia'),
    # path('arkansas/', get_arkansas, name='arkansas'),
    # path('kansas/', get_kansas, name='kansas'),
    # path('georgia_drill_down/', get_georgia_advanced, name='georgia_advanced'),
    path('united_states/', UnitedStates.as_view(), name='usa')
]