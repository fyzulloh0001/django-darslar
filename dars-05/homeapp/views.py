from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
def salom(request):
    return render(request=request,template_name='salom.html')

class alik(TemplateView):
    template_name='alik.html'
