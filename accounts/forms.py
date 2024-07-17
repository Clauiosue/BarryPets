from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Pet
from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=15, required=True, help_text='Required.')
    address = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'address', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        return password2

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'breed', 'species']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'species': forms.TextInput(attrs={'class': 'form-control'}),
        }