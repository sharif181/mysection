from django.shortcuts import render
from .models import Routine

def saturday(request):
    routines = Routine.objects.all()
    context = {
        'routines':routines,
        'day':"saturday"
    }
    print(context)
    return render(request,'routine.html',context)


def sunday(request):
    routines = Routine.objects.all()
    context = {
        'routines':routines,
        'day':"sunday"
    }
    print(context)
    return render(request,'routine.html',context)

def monday(request):
    routines = Routine.objects.all()
    context = {
        'routines':routines,
        'day':"monday"
    }
    print(context)
    return render(request,'routine.html',context)

def tuesday(request):
    routines = Routine.objects.all()
    context = {
        'routines':routines,
        'day':"tuesday"
    }
    print(context)
    return render(request,'routine.html',context)


def wednesday(request):
    routines = Routine.objects.all()
    context = {
        'routines':routines,
        'day':"wednesday"
    }
    print(context)
    return render(request,'routine.html',context)


def thrusday(request):
    routines = Routine.objects.all()
    context = {
        'routines':routines,
        'day':"thrusday"
    }
    print(context)
    return render(request,'routine.html',context)


def extra(request):
    routines = Routine.objects.all()
    context = {
        'routines':routines,
        'day':"extra"
    }
    print(context)
    return render(request,'routine.html',context)
