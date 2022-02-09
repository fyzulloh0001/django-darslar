from django.urls import path
from .views import salom,alik

urlpatterns = [
    path('',salom,name='salom'),
    path("alik/", alik.as_view(), name="alik")
]


