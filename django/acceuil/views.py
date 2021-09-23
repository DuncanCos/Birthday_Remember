from django.shortcuts import render
from addAnniv.models import donnee
from datetime import date
import datetime

# Create your views here.
def index (request):

    final=0
    mot = "nothing"
    first = 0
    last = 0
    soon = 1000
    if donnee.objects.exists():
        first = donnee.objects.first().id
        last = donnee.objects.last().id

# year-mounth-day
    d = str(datetime.date.today())
    day = d.split("-")

    month=day[1]
    Day=day[2]

    po = 0
    i = first
    while i!=last+1:
        #print(f"is {i} to {last + 1}")
        if donnee.objects.filter(pk=i).exists():
            yes=donnee.objects.get(pk=i)
            birthdate = yes.birthday
            birthDate = birthdate.split('/')
            dayDate = birthDate[0]
            monthDate = birthDate[1]

            d1 = date(2021,int(monthDate),int(dayDate))
            d2 = date.today()


            """
            fixer le probleme de soustraction

            la soustraction est tout le temp positif 
            trouver un moyen de faire en sorte de differencier les 
            anniversaire positif et negatif
            """

            result1 = abs(d1-d2).days
            print(abs(d2-d1).days)
            print (datetime.datetime.today().day)
            dt = datetime.datetime.today().day
            if result1 == 0:
                po = i
                soon = result1
                i += 1
            elif result1 > 0 and int(dayDate) > dt and result1 < soon:
                po = i
                soon = result1
                i += 1
            else:
                i += 1
        else:
            i += 1

    print(f"{po} and {soon}")

    if po == 0 and soon == 1000:
        mot= "no birthday today"
    elif po !=0 and soon > 0:
        motus= donnee.objects.get(pk=po).name
        
        mot = (f"it is the birthday of {motus} in {soon} days")
    else:
        motus= donnee.objects.get(pk=po).name
        mot=(f"THIS IS THE BIRTHDAY OF {motus} TODAY")
    
        
    return render (request, 'acceuil.html',{'mot': mot})
 