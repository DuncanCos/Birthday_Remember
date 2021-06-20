from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseRedirect
from .form import NameForm
from .models import donnee

# Create your views here.
def index (request):
    #print(donnee.objects.first().id)
    test="duncan"
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            ls=donnee()
            name= form.cleaned_data['name']
            surname= form.cleaned_data['surname']
            pseudo= form.cleaned_data['pseudo']

            #yes=donnee.objects.get(pk=5)
            #print(yes.name)

            #yes.delete()
            ls.name=name
            ls.pseudo=pseudo
            ls.save()
            return render(request, 'index.html' ,{'form': form,'wo':name,'wa': surname,'we':pseudo})
            #return render(request, 'index.html' ,{'form': form,'wo':test})
    else:
        form = NameForm()

    re = "nobody"
    return render(request, 'index.html' ,{'form': form,'wo':test, 'we': re})
