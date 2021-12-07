from django.db import models


class Resturant(models.Model):

    name = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.name} | {self.city}"
    
    def get_last_dishes(self):
        return self.dishes.all()[:3]

    def get_active_dishes(self):
        return self.dishes.filter(is_active=True).order_by("-created_at")