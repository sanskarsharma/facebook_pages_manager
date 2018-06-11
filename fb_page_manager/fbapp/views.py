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
    # details = {"data": [{"id": "946102352202285", "perms": ["ADMINISTER", "EDIT_PROFILE", "CREATE_CONTENT", "MODERATE_CONTENT", "CREATE_ADS", "BASIC_ADMIN"], "category": "Community", "access_token": "EAAGzj2LLCQYBAICnFi5k3j4yD6mKfM0yUVQIZAupwpOgwdmCiiMrAx3I7U32gYHZCplwruizxTHZCa5YRzJba1SsUcYr7rUnNM2b630FokZAPYLP0S556EvLPQraaozQeZAos1IYUKSUnZBTxB3ETaoZCivIIKVV9dEDWMiZBY3jfL7UU7r3hHu29OUK5FNBydujucPnwhCKOwZDZD", "name": "Placement Assistance Cell", "category_list": [{"id": "2612", "name": "Community"}]}], "paging": {"cursors": {"after": "OTQ2MTAyMzUyMjAyMjg1", "before": "OTQ2MTAyMzUyMjAyMjg1"}}}
    # d2 = { "name": "Sanskar Sharma", "id": "123123"}

    return render(request, "fbapp/dashboard.html",{'pages': details, 'personal':d2})

    #return render(request, "fbapp/dashboard.html")


def get_page_details(request):
	if request.method=='POST':
		fields='category,name,phone,general_info,about,bio,location,emails,website,description,company_overview'
		pageToken=request.POST.get("pageToken",'')
		pageId=request.POST.get("pageId",'')
		header='OAuth ' + pageToken
		url="https://graph.facebook.com/"+pageId + "?fields="+fields
		details=call('GET', url, headers={"Authorization": header})
		details=json.dumps(details.json())
		return HttpResponse(details)
	return HttpResponse(400)
