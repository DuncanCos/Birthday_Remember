from django.shortcuts import render, redirect
from addAnniv.models import donnee
from django.http import HttpResponse

# Create your views here.
def index (request):


    if donnee.objects.exists():
        c=donnee.objects.all()
    else:
        return render (request, 'nothing.html')

    return render (request, 'list.html', {'name':c})




def delete(request, delete):
    yes=donnee.objects.get(pk=delete)
    yes.delete()
    return redirect ("/showList/")
