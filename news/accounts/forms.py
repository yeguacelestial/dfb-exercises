from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# Add custom field to the default User model of Django
class CustomUserCreationForm(UserChangeForm):

    # Define model with new field, and add it to the UserCreatinForm
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', )


# Do the same, but now for Custom User Change form
class CustomUserChangeForm(UserChangeForm):

    class Meta():
        model = CustomUser
        fields = UserChangeForm.Meta.fields
