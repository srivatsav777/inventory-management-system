import ConfigParser as cp
import os
import json

file_desc=open('conf/conf.conf','r')
config = cp.ConfigParser()
config.read('conf/conf.conf') 
#return config['ip']
print config.get('section','ip_address')

n=config.get('section','number_of_transactions')
db=config.get('section','db')
IP=config.get('section','ip_address')
prt=config.get('section','port')
proxy=config.get('section','proxy')
pip=config.get('section','pip_address')
pport=config.get('section','pport')

rfobj('cassandra-stress write no-warmup n='+n+'-schema keyspace=reniacperf -node <'+db+' '+IP+'> -port native='+prt+'-col n=FIXED\(10\) size=FIXED\(400\) -rate threads=4 -pop dist=seq\(1..1000000\) ')

rfobj('cassandra-stress mixed ratio\(read=8, write=2\) no-warmup n='+n+'-schema keyspace=reniacperf -node <'+db+' '+IP+'> -port native='+prt+'-col n=FIXED\(10\) size=FIXED\(400\) -rate threads=16 -pop dist=seq\(1..1000000\) &>db.json')

rfobj('cassandra-stress read no-warmup n='+n+'-schema keyspace=reniacperf -node <'+proxy+' '+pip+'> -port native='+pport+'-col n=FIXED\(10\) size=FIXED\(400\) -rate threads=4 -pop dist=seq\(1..1000000\)')

rfobj('cassandra-stress mixed ratio\(read=8, write=2\) no-warmup n='+n+'-schema keyspace=reniacperf -node <'+proxy+' '+pip+'> -port native='+pport+'-col n=FIXED\(10\) size=FIXED\(400\) -rate threads=16 -pop dist=seq\(1..1000000\) &>cpx.json')




s1= json.load(open('db.json'))
s2= json.load(open('cpx.json'))

for x_val,y_val in zip(s1.iteritems(),s2.iteritems()):
  if(x_val==y_val):
    print 'Ok'
  else
    print 'Not Ok',x_val,y_val
