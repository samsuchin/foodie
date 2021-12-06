from django.urls import path, include
from .views import *

urlpatterns = [
    path("<resturant_pk>/", resturant_detail, name="resturant_detail")
]