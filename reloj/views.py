
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
    
def index(request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p %X", gmtime())
    }
    return render(request,'index.html', context)

def root(request):
    return redirect ("/")