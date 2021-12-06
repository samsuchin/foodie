from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path("@<username>", account_detail, name="account_detail"),
    path("", include('django.contrib.auth.urls')),
    path("accounts/login/", auth_views.LoginView.as_view(form_class=LoginForm)),
    path('signup/', signup, name="signup"),
]