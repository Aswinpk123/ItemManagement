from django.urls import path
from .views import *

urlpatterns  = [
    path('charge/',ChargesAPI.as_view()),
]