from django.urls import path
from .views import IndexView
from django.views.generic import TemplateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('map_app/USA.html', TemplateView.as_view(template_name='map_app/USA.html'), name='USA')
]