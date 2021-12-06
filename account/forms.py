from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate

# Create Login Form checking if user is active and getting the username and password in the login form
class LoginForm(AuthenticationForm):

    error_messages = {
        'invalid_login': 
            "Please make sure you entered the right username and password. "
        ,
        'inactive': "Oh no! This account is not active.",
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            user_obj = get_object_or_404(get_user_model(), username=username)
            if not user_obj.is_active:
                raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
                )
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=254, label="Username",)
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2',)
