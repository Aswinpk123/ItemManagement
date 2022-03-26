from django.urls import path
from .views import *


urlpatterns = [
    path('details/',DetailsAPI.as_view()),
    path('documents/',DocumetsAPI.as_view()),
]