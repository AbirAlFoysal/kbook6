from django import forms
from .models import BookSearch
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookSearchForm(forms.ModelForm):
    name_of_book = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Enter name of book'
    }))
    class Meta:
        model = BookSearch
        fields = ['name_of_book',]


