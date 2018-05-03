# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import NameForm
import MySQLdb
import requests
import json
from .forms import NameProduct


def order_products(request):
    if(request.method=="GET"):
       form=NameForm()
       return render(request,"templates/fill.html",{'form':form})
    else:
       headers={'Content-Type':'application/json'}
       payload={"variables":{"name":{"value":request.POST.get("name")},"id":{"value":request.POST.get("id")},"product":{"value":request.POST.get('product')},"quantity":{"value":request.POST.get('quantity')}}}
       r=requests.post('http://localhost:8080/engine-rest/process-definition/key/invent_manage_system/start',data=json.dumps(payload),headers=headers)
       return HttpResponse('Your Order is recieved.')
    

def pro_det(request):
    if(request.method=="GET"):
       form=NameProduct()
       return render(request,"templates/product_details.html",{'form':form})
    else:
      db = MySQLdb.connect("localhost","root","root","inventory_management" )
      cursor = db.cursor()
      cursor.execute("insert into products(ProductName,PartNumber,ProductLabel) values('"+request.POST.get('pname')+"','"+request.POST.get('pnum')+"','"+request.POST.get('plabel')+"');")
      db.commit();
      db.close();      
      return HttpResponse('Your Product is added successfully.')
   


def view_orders(request):
   if(request.method=="GET"):
     r=requests.get('http://localhost:8080/engine-rest/task?processDefinitionKey=invent_manage_system')  
     x=r.json()
     l=[]
     l2=[]
      
     for p in x:
       temp=requests.get('http://localhost:8080/engine-rest/task/'+p['id']+'/variables')
       t=temp.json()
       if(len(t)<=4):
         l2.append(p["id"])
         l.append(t)
     
     context={"dic1":zip(l,l2)}
     return render(request,'templates/disp.html',context)
      

def approve_order(request):
   if(request.method=="POST"):
     temp=requests.get('http://localhost:8080/engine-rest/task/'+str(request.POST.get('id'))+'/variables')
     t=temp.json()
     print t['product']
     db = MySQLdb.connect("localhost","root","root","inventory_management" )
     cursor = db.cursor()
     a=t['product']['value']
     b=t['quantity']['value']
     cursor.execute("select InventoryOnHand from products where ProductName='"+a+"'")
     data=list(cursor.fetchone())
     ev=int(data[0])
     print 'stock',ev,'asked',b
     if(ev>=int(b)):
       cursor.execute("update products set InventoryOnHand="+str(ev-int(b))+" where ProductName='"+a+"'")       
       db.commit()
       db.close()
       headers={'Content-Type':'application/json'}
       payload={"variables":{"approve":{"value":True}}}
       r=requests.post("http://localhost:8080/engine-rest/task/"+str(request.POST.get('id'))+"/complete",data=json.dumps(payload),headers=headers)
       r=requests.post("http://localhost:8080/engine-rest/task/"+str(request.POST.get('id'))+"/complete",data=json.dumps(payload),headers=headers)
       return HttpResponse('Order is approved')
     else:
       headers={'Content-Type':'application/json'}
       payload={"variables":{"approve":{"value":False}}}
       r=requests.post("http://localhost:8080/engine-rest/task/"+str(request.POST.get('id'))+"/complete",data=json.dumps(payload),headers=headers)
       r=requests.post("http://localhost:8080/engine-rest/task/"+str(request.POST.get('id'))+"/complete",data=json.dumps(payload),headers=headers)
       return HttpResponse('Sorry. We dont have enough stock.')
     
    

def hello(request):
   if(request.method=="GET"):
      db = MySQLdb.connect("localhost","root","root","inventory_management" )
      cursor = db.cursor()
      cursor.execute("SELECT * from products")
      data1= cursor.fetchall()
      #print "Database version : %s " % data
   
      #cursor = db.cursor()
      cursor.execute("select purchases.PurchaseDate,products.ProductName,purchases.NumberReceived,(select supplier from suppliers where suppliers.id=purchases.SupplierId) as supplier  from products INNER JOIN purchases on products.id=purchases.ProductId ORDER BY  products.ProductName;")
      data2= cursor.fetchall()
      data2=list(data2)

   
      #cursor = db.cursor()
      cursor.execute("SELECT * from orders;")
      data3= cursor.fetchall()
   

      cursor.execute("select ProductName,count(ProductName),sum(NumberReceived) as numberofpurchases from v GROUP BY ProductName;")
      data4= cursor.fetchall()
      i=0
      for row in data4:
            data2.insert(i,row)
            i+=row[1]+1
      #cursor = db.cursor()
      #cursor.execute("SELECT * from orders")
      #data = cursor.fetchall()

      db.close()
      context={'data1':data1,'data2':data2,'data3':data3}
      return render(request,'templates/sample.html',context)
   else:
      db = MySQLdb.connect("localhost","root","root","inventory_management" )
      cursor = db.cursor()
      x1=int(request.POST.get('v1'))
      x2=request.POST.get('v2')
      x3=request.POST.get('v3')
      x4=request.POST.get('v4')
      x5=int(request.POST.get('v5'))
      x6=int(request.POST.get('v6'))
      x7=int(request.POST.get('v7'))
      x8=int(request.POST.get('v8'))
      x9=int(request.POST.get('v9'))

      cursor.execute("select version()")
      print(cursor.fetchone())
      #print("update products  set %s='%s' where id=%d ;  " %(request.POST.get('clmn'),request.POST.get('val'),int(request.POST.get('rw'))))
      if cursor.execute("update products  set id=%d,ProductName='%s',PartNumber='%s',ProductLabel='%s',StartingInventory=%d,InventoryReceived=%d,InventoryShipped=%d,InventoryOnHand=%d,MinimumRequired=%d where id=%d ; " %(x1,x2,x3,x4,x5,x6,x7,x8,x9,x1)):
          print "updated"
      db.commit()
      db.close()
      return HttpResponse('stored') 
