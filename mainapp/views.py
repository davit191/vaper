from django.shortcuts import render
from .models import category,news, personal,social,slide,data_contact


# Create your views here.
def home(request):
    new = news.objects.all()[:5]
    return render(request,'mainapp/index.html',{'news':new})

def getCategory(request, slug):
    cat = category.objects.get(slug=slug)
    return render(request,'mainapp/products.html', {'cat':cat})


def newser(request,id):
    dav= news.objects.get(id=id)
    return render(request,'mainapp/new_prod.html',{'news':dav})


def ollnews(request):
    oll = news.objects.all()
    return render(request,'mainapp/newsoll.html',{'news':oll})

def contakt(request):
    pers  = personal.objects.all()
    return render( request,"mainapp/contacts.html" ,{'personal':pers})

def slayder(request):
    slid = slide.objects.all() 

    return render(request,"base.html",{"slid":slid})