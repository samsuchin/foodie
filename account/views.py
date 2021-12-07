from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.db.models import Q
from .forms import SignUpForm
from dish.models import Save
from dish.models import Dish

# Get someones account info. Fetch their posts, but if it's their own account also fetch their saved dishes and resturants and render a different template.
def account_detail(request, username):
    # Get account based on username
    account = get_object_or_404(get_user_model(), username=username)
    context = {
        "account": account,
        "saved_performances": Dish.objects.filter(saves__saved_by=request.user).order_by("-pk")
    }
    # If the user owns the account display that specific template
    if account==request.user:
        context["user_saves"] = Save.objects.filter(saved_by=request.user).values_list("dish_id", flat=True)
        return render(request, "account/personal.html", context)
    # Else do detail template
    else:
        return render(request, "account/detail.html", context)


def signup(request):
    # If a user posts then grab the data through django forms, see if valid. If is, login and redirect
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            account = form.save()
            login(request, account)

            return redirect("home")
    else:
        # Provide django forms signup
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
