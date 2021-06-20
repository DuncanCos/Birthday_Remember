from django.shortcuts import render
from addAnniv.models import donnee

# Create your views here.
def index (request, num):

    final="0"
    mot = "nothing"

    if donnee.objects.exists():
        c=donnee.objects.all()
        theId = donnee.objects.first().id
        theLast = donnee.objects.last().id
        final=   1+theLast - theId



    mot="there is {} people in the list".format(final)







    return render (request, 'acceuil.html',{'mot': mot})
