from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from requests import request as call
import json

# Create your views here.

def home(request):
    context = {
        "user_name" : "chotu"
    }
    # my_template = loader.get_template("fbapp/home.html")  # old-way
    # return HttpResponse(my_template.render(context,request))
    return render(request, "fbapp/home.html", context)

def dashboard(request):
    token=request.POST.get("token",'')
    header="OAuth "+ token
    details=call('GET', 'https://graph.facebook.com/me/accounts', headers={"Authorization": header})
    d2=call('GET','https://graph.facebook.com/me', headers={"Authorization":header})
    details=json.dumps(details.json())
    d2=json.dumps(d2.json())
    print(details)
    return render(request, "dashboard.html",{'pages': details, 'personal':d2})

    #return render(request, "fbapp/dashboard.html")