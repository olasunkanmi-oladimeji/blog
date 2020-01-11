from .models import commentpost
from django import forms
from django.forms import ModelForm
class commentform(forms.ModelForm):
    
    class Meta:
        model = commentpost
        fields = ( 'name','comment')