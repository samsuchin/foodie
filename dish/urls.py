from django.urls import path, include
from .views import *

urlpatterns = [
    path("post/", post, name="post"),
    path("save/", change_save_dish, name="change_save_dish"),
    path("delete/<dish_pk>/", delete, name="delete_dish")
]