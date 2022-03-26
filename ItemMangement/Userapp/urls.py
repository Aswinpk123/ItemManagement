from django.urls import path
from .views import *

urlpatterns = [
    path('user/',UserAPI.as_view()),
    path('login/',LoginView.as_view()),
    path('who/',WhoAmI.as_view()),
    path('logout/',Logout.as_view()),
]