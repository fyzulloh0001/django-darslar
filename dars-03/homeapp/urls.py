from django.urls import path
from .views import fayzulloh

urlpatterns = [
    path('',fayzulloh.as_view(),name='home')
]
