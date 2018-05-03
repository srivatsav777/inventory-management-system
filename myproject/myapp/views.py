# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests

# Create your views here.

def hello(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    #today= datetime.datetime.now().date()
    return render(request,'templates/demo.html',{
        "ip": geodata['ip'],
        "country": geodata['country_name'],
       # "today" : today
    })
