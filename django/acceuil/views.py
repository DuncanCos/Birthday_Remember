from django.shortcuts import render
from addAnniv.models import donnee
import datetime

# Create your views here.
def index (request, num):

    final=0
    mot = "nothing"
    print(datetime.date.today())
    first=0
    last=0

    if donnee.objects.exists():
        first = donnee.objects.first().id
        last = donnee.objects.last().id

# year-mounth-day
    d = str(datetime.date.today())
    day = d.split("-")

    print(day[0])

    month=day[1]
    Day=day[2]

    po = 0
    i = first
    while i!=last+1:
        print(i)
        if donnee.objects.filter(pk=i).exists():
            yes=donnee.objects.get(pk=i)
            birthdate = yes.birthday
            birthDate = birthdate.split('/')
            dayDate = birthDate[0]
            monthDate = birthDate[1]
            final+=1
            if monthDate == month and dayDate == Day:
                po=i
            i+=1
        else:
            i+=1

    if po == 0:
        motus = "nobody"
    else:
        motus= donnee.objects.get(pk=po).name
    mot="THIS IS THE BIRTHDAY OF {} TODAY".format(motus)




    return render (request, 'acceuil.html',{'mot': mot})
