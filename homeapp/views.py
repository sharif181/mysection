from django.shortcuts import render
from .models import quiz,presentation,assignment,Announcement
from datetime import date

def index(request):
    quc=0
    prec=0
    assic=0
    As= Announcement.objects.all()
    Date = date.today()
    quizs = quiz.objects.all()
    presentations = presentation.objects.all()
    assignments = assignment.objects.all()

    for q in quizs:
        if Date <= q.date:
            quc+=1
    for q in presentations:
        if Date <= q.date:
            prec+=1
    for q in assignments:
        if Date <= q.lastDate:
            assic+=1


    return render(request,'index.html',{'qc':quc , 'pc':prec, 'ac':assic , 'As':As, 'date':Date})

def Quiz(request):

    Quizs= quiz.objects.all()
    Date = date.today()
    return render(request, 'quiz.html',{'quiz':Quizs, 'Date':Date})

def Presentation(request):
    presentations = presentation.objects.all()
    Date = date.today()
    return render(request, 'presentation.html', {'Presentations': presentations, 'Date': Date})

def Assignment(request):
    assignments = assignment.objects.all()
    Date = date.today()
    return render(request, 'assignment.html', {'assignments': assignments, 'Date': Date})