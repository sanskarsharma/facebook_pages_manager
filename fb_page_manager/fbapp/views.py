from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from requests import request as call
import json
from . import forms
# Create your views here.


def home(request):
    context = {
        "title":"FB Page Manager"
    }
    # my_template = loader.get_template("fbapp/home.html")  # old-way
    # return HttpResponse(my_template.render(context,request))
    return render(request, "fbapp/home.html", context)


def dashboard(request):
    if(request.method=="POST"):
        token=request.POST.get("token",'')
        header="OAuth "+ token
        details=call('GET', 'https://graph.facebook.com/me/accounts', headers={"Authorization": header})
        d2=call('GET','https://graph.facebook.com/me', headers={"Authorization":header})
        details=json.dumps(details.json())
        d2=json.dumps(d2.json())
        #print(details)
        #pages = details["data"]
        # mega_details = {}
        # for each_page in pages:
        #     data_dict = {}
        #     data_dict["pageToken"] = each_page["access_token"]
        #     data_dict["pageId"] = each_page["id"]
        #     res_dict = call("POST", "/fbapp/page_detail", data=data_dict)
        #     mega_details[each_page["id"]] = res_dict
        # details = {"data": [{"id": "946102352202285", "perms": ["ADMINISTER", "EDIT_PROFILE", "CREATE_CONTENT", "MODERATE_CONTENT", "CREATE_ADS", "BASIC_ADMIN"], "category": "Community", "access_token": "EAAGzj2LLCQYBAICnFi5k3j4yD6mKfM0yUVQIZAupwpOgwdmCiiMrAx3I7U32gYHZCplwruizxTHZCa5YRzJba1SsUcYr7rUnNM2b630FokZAPYLP0S556EvLPQraaozQeZAos1IYUKSUnZBTxB3ETaoZCivIIKVV9dEDWMiZBY3jfL7UU7r3hHu29OUK5FNBydujucPnwhCKOwZDZD", "name": "Placement Assistance Cell", "category_list": [{"id": "2612", "name": "Community"}]}], "paging": {"cursors": {"after": "OTQ2MTAyMzUyMjAyMjg1", "before": "OTQ2MTAyMzUyMjAyMjg1"}}}
        # d2 = { "name": "Sanskar Sharma", "id": "123123"}
        return render(request, "fbapp/dashboard.html",{"title":"Dashboard",'pages': details, 'personal':d2}) #, 'mega_details': mega_details})
    else:
        # here use sessions to save user-id and pageids/tokens
        details = {}
        d2 = {}
        return render(request, "fbapp/dashboard.html",{"title":"Dashboard",'pages': details, 'personal':d2}) #, 'mega_details': mega_details})

    #return render(request, "fbapp/dashboard.html")

@csrf_exempt
def get_page_details(request):
    if request.method=="POST":
        print("HELLO")
        fields='name,general_info,about,bio,impressum,phone,whatsapp_number,emails,website,description,company_overview,fan_count,link,overall_star_rating,rating_count,displayed_message_response_time,is_published,verification_status,location'
        pageToken=request.POST.get("pageToken",'')
        pageId=request.POST.get("pageId",'')
        header='OAuth ' + pageToken
        url="https://graph.facebook.com/"+pageId + "?fields="+fields
        details=call('GET', url, headers={"Authorization": header})

        details=json.dumps(details.json())
        return HttpResponse(details)
    return HttpResponse(400)

#not used
def get_form(request):
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     d = {}
    #     if request.GET.get('access_token_for_update','') is not None:
    #         d['access_token_for_update']=request.GET.get('access_token_for_update','')
    #     if request.GET.get('page_id_for_update','') is not None:
    #         d['page_id_for_update']=request.GET.get('page_id_for_update','')
    #     if request.GET.get('name','') is not None:
    #         d['name']=request.GET.get('name','')
    #     if request.GET.get('about','') is not None:
    #         d['about']=request.GET.get('about','')
    #     if request.GET.get('bio','') is not None:
    #         d['bio']=request.GET.get('bio','')
    #     if request.GET.get('website','') is not None:
    #         d['website']=request.GET.get('website','')
    #     if request.GET.get('phone','') is not None:
    #         d['phone']=request.GET.get('phone','')
    #     if request.GET.get('whatsapp_number','') is not None:
    #         d['whatsapp_number']=request.GET.get('whatsapp_number','')
    #     if request.GET.get('general_info','') is not None:
    #         d['general_info']=request.GET.get('general_info','')
    #     if request.GET.get('impressum','') is not None:
    #         d['impressum']=request.GET.get('impressum','')
    #     if request.GET.get('description','') is not None:
    #         d['description']=request.GET.get('description','')
    #     if request.GET.get('company_overview','') is not None:
    #         d['company_overview']=request.GET.get('company_overview','')

    #     form = forms.SimpleForm(initial=d)

    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('/dashboard/')
    # else:

    id = request.GET.get("id",'')
    form = forms.SimpleForm()

    return render(request, 'fbapp/pageform.html', {'form_obj': form})


