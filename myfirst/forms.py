from django import forms
from django.forms import fields
from .models import Posts


class InputForm(forms.Form):
    title = forms.CharField(max_length=5)
    body = forms.CharField(max_length=500,widget=forms.Textarea)


class InputFormModel(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"
