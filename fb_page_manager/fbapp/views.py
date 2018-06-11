from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from requests import request as call
import json
from . import forms
# Create your views here.

global_dict ={}

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

    return render(request, "fbapp/dashboard.html",{'pages': details, 'personal':d2}) #, 'mega_details': mega_details})

    #return render(request, "fbapp/dashboard.html")

# @csrf_exempt
# def get_page_details(request):
# 	if request.method=='POST':
# 		fields='name,general_info,about,bio,impressum,phone,whatsapp_number,emails,website,description,company_overview,displayed_message_response_time,fan_count,link,overall_star_rating,rating_count,verification_status,is_published'
#         # category, location
# 		pageToken=request.POST.get("pageToken",'')
# 		pageId=request.POST.get("pageId",'')
# 		header='OAuth ' + pageToken
# 		url="https://graph.facebook.com/"+pageId + "?fields="+fields
# 		details=call('GET', url, headers={"Authorization": header})
# 		details=json.dumps(details.json())

# 		return HttpResponse(details)
# 	return HttpResponse(400)

@csrf_exempt
def get_page_details(request):
    if request.method=="POST":
        print("HELLO")
        fields='name,general_info,about,bio,impressum,phone,whatsapp_number,emails,website,description,company_overview,displayed_message_response_time,fan_count,link,overall_star_rating,rating_count,verification_status,is_published'
        pageToken=request.POST.get("pageToken",'')
        pageId=request.POST.get("pageId",'')
        header='OAuth ' + pageToken
        url="https://graph.facebook.com/"+pageId + "?fields="+fields
        details=call('GET', url, headers={"Authorization": header})

        global_dict["pageId"]= details.json()

        details=json.dumps(details.json())
        return HttpResponse(details)
    return HttpResponse(400)

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
    form = forms.SimpleForm(initial=global_dict[id])
    
    return render(request, 'fbapp/pageform.html', {'form_obj': form})



def update_page_details(request):
	d={}
	pageToken=request.POST.get("access_token",'')
	pageId=request.POST.get("page_id",'')
	d1={}
	d['access_token']=pageToken
	if request.POST.get("phone") is not None:
		d['phone']=request.POST.get("phone",'')
	if request.POST.get("emails") is not None:
		d['emails']=request.POST.get("emails",'')
	if request.POST.get("general_info") is not None:
		d['general_info']=request.POST.get("general_info",'')
	if request.POST.get("about") is not None:
		d['about']=request.POST.get("about",'')
	if request.POST.get("bio") is not None:
		d['bio']=request.POST.get("bio",'')
	if request.POST.get("website") is not None:
		d['website']=request.POST.get("website",'')
	if request.POST.get("description") is not None:
		d['description']=request.POST.get("description",'')
	if request.POST.get("company_overview") is not None:
		d['company_overview']=request.POST.get("company_overview",'')
	if request.POST.get("lname") is not None:
		d1['name']=request.POST.get("lname")
	if request.POST.get("city") is not None:
		d1['city']=request.POST.get("city")
	if request.POST.get("state") is not None:
		d1['state']=request.POST.get("state")
	if request.POST.get("country") is not None:
		d1['country']=request.POST.get("country")
	if request.POST.get("street") is not None:
		d1['street']=request.POST.get("street")
	if request.POST.get("zip") is not None:
		d1['zip']=request.POST.get("zip")
			
	# d['location']=d1
	print(d)
	# header='OAuth ' + pageToken
	# url="https://graph.facebook.com/"+pageId
	# urll=url+"/location"
	# details1=call('POST', url, data=d1, headers={"Authorization":header})
	# details=call('POST', url,data=d, headers={"Authorization": header})
	return HttpResponse(json.dumps(d.json()))

