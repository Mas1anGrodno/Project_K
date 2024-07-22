from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    html = "<html><body><img src='https://upyachka.io/img/kot/77.gif' alt=\"UPYACHKA\"></body></html>"
    return HttpResponse(html)

