from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    birthday = forms.CharField(label='date of birthday', max_length=10)