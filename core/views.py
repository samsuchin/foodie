from django.shortcuts import render

from dish.models import Dish, Save

# Create your views here.

def home(request):
    # Grab random active dishes to display on home for user
    dishes = Dish.objects.filter(is_active=True).order_by("?")[:20]

    # Pass the data to the template
    context = {
        "dishes": dishes,
    }
    if request.user.is_authenticated:
        context["user_saves"] = Save.objects.filter(saved_by=request.user).values_list("dish_id", flat=True)

    return render(request, "index.html", context)