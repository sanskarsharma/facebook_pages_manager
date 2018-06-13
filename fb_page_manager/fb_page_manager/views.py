from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from requests import request as call
import json

def startpage(request):
    return HttpResponseRedirect("/fbapp")