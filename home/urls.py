from django.urls import path
from .views import homedisplay

urlpatterns = [
    path('', homedisplay, name='homesite1'),
]
