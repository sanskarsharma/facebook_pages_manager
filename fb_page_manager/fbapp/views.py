from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    context = {
        "user_name" : "chotu"
    }
    # my_template = loader.get_template("fbapp/home.html")  # old-way
    # return HttpResponse(my_template.render(context,request))
    return render(request, "fbapp/home.html", context)

def dashboard(request):
    return render(request, "fbapp/dashboard.html")