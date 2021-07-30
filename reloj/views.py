
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, localtime, strftime
from django.utils import timezone

    
def index(request):
    print(timezone.now())
    context = {
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%I:%M %p %X", localtime()),
    }
    return render(request,'index.html', context)

def root(request):
    return redirect ("/")