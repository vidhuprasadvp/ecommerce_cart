from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def living(request):
    return render(request,'living.html')

def bedroom(request):
    return render(request,'bedroom.html')


def decor(request):
    return render(request,'decor.html')

def kitchen(request):
    return render(request,'kitchen.html')

def light(request):
    return render(request,'light.html')

def mattres(request):
    return render(request,'mattres.html')

def office(request):
    return render(request,'office.html')


def outdoor(request):
    return render(request,'outdoor.html')



