from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Register new users
class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User
        # Password2 = password confirmation
        fields = ['username', 'email', 'password1', 'password2']

# Update existing users
class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta():

        model = User
        fields = ['username', 'email']



