from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, 'project_K/main.html')

def test(request):
    return HttpResponse(f"<h1> TSTSTSTST </h1>")