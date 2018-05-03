# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import processes
from .serializers import processesSerializer
from .models import instances
from .serializers import instancesSerializer
from .models import task
from .serializers import taskSerializer
import json
from django.core import serializers
import requests
from .forms import NameForm
from django.http import HttpResponseRedirect

def post(request):
   headers={'Content-Type':'application/json'}
   payload={"variables":{"name":{"value":form['fields'].name},"percentage":{"value":form['fields'].name}}}
   r=requests.post('http://localhost:8080/engine-rest/process-definition/key/internship/start',data=json.dumps(payload),headers=headers)
   return HttpResponse('<h1> Sucessfully created process </h1>')



def get_form_data(request):
    if(request.method== "GET" ):
       form=NameForm() 
       return render(request,'templates/name.html',{'form':form})
    else:
       #form=NameForm(request.POST)
       #if(form.is_valid()) :
       #       form.cleaned_data
       headers={'Content-Type':'application/json'}
       #      x=json.dumps(request.POST)
       #       x=json.loads(x)
       payload={"variables":{"name":{"value":request.POST.get('name')},"percentage":{"value":request.POST.get('percentage')}}}
       r=requests.post('http://localhost:8080/engine-rest/process-definition/key/internship/start',data=json.dumps(payload),headers=headers)
       return HttpResponse('Sucessfully created process')


class processList(APIView):

   def get(self,request):
     r=requests.get('http://localhost:8080/engine-rest/task?processDefinitionKey=internship')  
     x=r.json()
     context={"dic": x}
     return render(request,'templates/form.html',context)

   def post(self):
     pass #request.post('localhost:8080/engine-rest/process-definition/key/internship/start')

class instanceList(APIView):

   def get(self,request):
     p1=instances.objects.all()
     serializer=instancesSerializer(p1,many=True)
     return Response(serializer.data)    

   def post(self):
    pass 

class taskList(APIView):

   def get(self,request):
     p1=task.objects.all()
     serializer=taskSerializer(p1,many=True)
     return Response(serializer.data)    

   def post(self):
    pass 

