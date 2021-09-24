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
            birthday= form.cleaned_data['birthday']

            #yes=donnee.objects.get(pk=5)
            #print(yes.name)

            #yes.delete()
            ls.name=name
            ls.birthday=birthday
            ls.save()
            return render(request, 'index.html' ,{'form': form,'wo':name,'we':birthday})
            #return render(request, 'index.html' ,{'form': form,'wo':test})
    else:
        form = NameForm()

    re = "never"
    return render(request, 'index.html' ,{'form': form,'wo':test, 'we': re})
