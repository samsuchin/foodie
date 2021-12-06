from django.shortcuts import render, get_object_or_404
from .models import Resturant
from dish.models import Save

def resturant_detail(request, resturant_pk):
    resturant = get_object_or_404(Resturant, pk=resturant_pk)
    context = {
        "resturant": resturant,
    }
    if request.user.is_authenticated:
        context["user_saves"] = Save.objects.filter(saved_by=request.user).values_list("dish_id", flat=True)
    return render(request, "resturant/detail.html", context)