from rest_framework.urls import path
from .views import *

urlpatterns = [
    path('status/',StatusAPI.as_view()),
    path('job/',JobsAPI.as_view()),
    path('report/',ReportAPI.as_view()),
   
]