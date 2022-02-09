from django.urls import path
from .views import fayzulloh

urlpatterns = [
    path('',fayzulloh,name='home')
]
