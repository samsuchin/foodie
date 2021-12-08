from django.contrib.auth import get_user_model
from django.db import models
from resturant.models import Resturant
from . import DISH
from django.conf import settings


class Dish(models.Model):

    name = models.CharField(max_length=255)
    media = models.ImageField(upload_to="dishes/")
    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE, related_name="dishes")
    review = models.TextField(null=True, blank=True, max_length=1000)
    rating = models.CharField(choices=DISH.RATING_CHOICES, max_length=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="dishes")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name


class Save(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="saves")
    created_at = models.DateTimeField(auto_now_add=True)
    saved_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "{} -> {}".format(self.saved_by, self.dish)