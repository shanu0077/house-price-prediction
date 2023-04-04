from django.shortcuts import render
from accounts.models import Appartment


def index(request):
    appartments = Appartment.objects.all()
    return render(request,'index.html', {'appartments': appartments})

