from django import forms
from django.forms import TextInput


class BlogForm(forms.Form):
    category = forms.CharField(label='Category', max_length=255,
                               widget=TextInput(attrs=({'class': "form-control pill inp", "placeholder": "Category"})))
    keywords = forms.CharField(label='Keywords', max_length=255,
                               widget=TextInput(attrs=({'class': "form-control pill inp", "placeholder": "Keyword"})))
