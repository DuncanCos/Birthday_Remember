from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    surname = forms.CharField(label='Your surname', max_length=100)
    pseudo = forms.CharField(label='Your pseudo', max_length=100)
