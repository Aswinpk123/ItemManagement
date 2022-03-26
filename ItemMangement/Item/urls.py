from django.urls import path
from .views import *

urlpatterns = [
    path("Itemtypedata/",ItemTypeAPI.as_view()),
    path("Itemdata/",ItemAPI.as_view()),
]