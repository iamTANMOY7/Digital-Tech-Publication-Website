from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput)
    last_name = forms.CharField(required=False, widget=forms.TextInput)
    email = forms.EmailField(
        required=True, label=("Email Address"), widget=forms.EmailInput
    )
    password1 = forms.CharField(
        required=True, label=("Create Password"), widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        required=True, label=("Confirm Password"), widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'username': None,  # This will remove the default help text
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
