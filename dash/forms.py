from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

choices =  category.objects.all().values_list('name','name')

choices_list = []

for item in choices:
    choices_list.append(item)

class PostForm(ModelForm):
    class Meta:
        model = post
        fields = ('title', 'aurthor', 'category','body')

        widgets  = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'we move'}),
            'aurthor': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user_name' , 'type': 'hidden'}),
            'category': forms.Select(choices=choices_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }


class EditForm(ModelForm):
    class Meta:
        model = post
        fields = ('title','body')
        widgets  = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'this is me'}),
            'aurthor': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }



