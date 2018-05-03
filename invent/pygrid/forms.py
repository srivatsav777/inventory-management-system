from django import forms
import MySQLdb

db = MySQLdb.connect("localhost","root","root","inventory_management" )
cursor = db.cursor()
cursor.execute("SELECT ProductName from products")
data1=list(cursor.fetchall())
Products=[]
for x in data1:
 s=x[0].lower()
 t=(s,x[0])
 Products.append(t)
 print Products
db.close()


class NameForm(forms.Form):
    name=forms.CharField(label="Customer Name",max_length=100)
    cus_id=forms.CharField(label="Customer id",max_length=10)
    product= forms.CharField(label='Product', widget=forms.Select(choices=Products))
    quantity=forms.IntegerField(label="quantity")
    

class NameProduct(forms.Form):
    pname=forms.CharField(label="Product Name",max_length=100)
    pnum=forms.CharField(label="Part Number",max_length=20)
    plabel= forms.CharField(label='Product Label',max_length=20)

