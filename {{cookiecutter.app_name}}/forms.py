from django import forms
from .models import {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}Form(forms.ModelForm):
	
	name = forms.CharField(widget=forms.TextInput(attrs={'autofocus':''}))

    class Meta:
        model = {{ cookiecutter.model_name }}
        fields = ['name', ]
