from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    params = {
        'title': 'Matching Place',
    }
    return render(request,'index.html',params)

def member_register(request):
    params = {
        'title': 'Register Member',
    }
    return render(request,'index.html',params)

def place_register(request):
    params = {
        'title': 'Register Place',
    }
    return render(request,'index.html',params)
