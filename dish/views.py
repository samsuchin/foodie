from django.contrib.messages import success
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from resturant.models import Resturant
from .models import Dish, Save
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json

# Make sure user is logged in to post and redirect if not
# Post dishes from different resturants and upload content
@login_required
def post(request):
    # If post is done, get all the form data
    if request.method=="POST":
        name = request.POST.get("name")
        resturant_pk = request.POST.get("resturant_pk")
        media = request.FILES.get("media")
        review = request.POST.get("review", None)
        rating = request.POST.get("rating")
        price = request.POST.get("price", None)
        # Get resturant and if doesnt exist then throw error
        resturant = get_object_or_404(Resturant, pk=resturant_pk)
        # Create new dish with provided info
        dish = Dish.objects.create(
            name=name,
            resturant=resturant,
            media=media,
            review=review,
            rating=rating,
            price=price,
            user=request.user
        )
        # Throw a success message and redirect to resturant detail page
        success(request, f"Added new dish at {resturant.name}")
        return redirect(reverse("resturant_detail", kwargs={"resturant_pk": resturant_pk}))

    # Display resturants
    resturants = Resturant.objects.filter(is_active=True).order_by("-created_at")
    context = {
        "resturants": resturants
    }
    return render(request, "post.html", context)

def change_save_dish(request):

    if request.method=="POST":
        data = json.loads(request.body)
        dish_pk = data.get("dish_pk")
        new_like, created = Save.objects.get_or_create(
                saved_by=request.user,
                dish_id=dish_pk
            )
        if created:
            liked = True
        else:
            liked = False
            new_like.delete()
        print(liked)
        return JsonResponse(liked, safe=False)

def delete(request, dish_pk):
    # Get dish
    dish = get_object_or_404(Dish, pk=dish_pk)
    # Make sure uer who is deleting owns the dish
    if request.user == dish.user:
        dish.delete()
        return redirect(reverse("account_detail", kwargs={"username": request.user.username}))
