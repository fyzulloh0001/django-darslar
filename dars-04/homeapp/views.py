from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
def fayzulloh(request):
    return HttpResponse("asslomu allaykum")

class ViewTemplate(TemplateView):
    template_name='home.html'