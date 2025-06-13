from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    #return render(request,'index.html')
    return render(request,'resume.html')



def server(request):
    return HttpResponse("<h2>HI,how are you</h2>")



    