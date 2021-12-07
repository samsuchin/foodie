from django.shortcuts import render
from django.db.models import Q
from resturant.models import Resturant

# Display random resturants and then allow user to query for specific ones and types
def explore(request):

    # Get search parameter and Q filter resturants
    search = request.GET.get("search", "")
    resturants = Resturant.objects.filter(is_active=True).filter(
    Q(name__icontains=search)|
    Q(cuisine__icontains=search)|
    Q(dishes__name__icontains=search)|
    Q(city__icontains=search)).order_by("?").distinct()
    
    context = {
        "resturants": resturants
    }
    return render(request, "explore.html", context)