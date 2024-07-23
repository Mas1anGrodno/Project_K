from django.urls import path

from .views import main
from .views import test

urlpatterns = [
    path("", main),
    #path("", test),
    
]