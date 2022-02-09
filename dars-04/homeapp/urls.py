from django.urls import path
from .views import fayzulloh,ViewTemplate


urlpatterns = [
    path('',fayzulloh,name='home'),
    path('alik/',ViewTemplate.as_view(),name='user')
]
