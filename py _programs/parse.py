#!/usr/bin/env python
import argparse
import sys
import os
import yaml   
import urllib

parser = argparse.ArgumentParser()
parser.add_argument('--yaml', default='test.yaml',help='Specify --yaml .yaml file path')
parser.add_argument('--proxy_name',help='Specify --proxy_name proxy ')
args = parser.parse_args()
#print args.conf,args.proxy_name

def systemCheck():
    # check for python 2.7.x if not give the error message and exit.
    # List of dependent modules
    # metric services and cassandra services
    #stat
    pass        

def bMetricServiceRunning():
   conn=urllib.urlopen('http://127.0.0.1') 
   if conn.getcode()==200:  
     return True
   else:
     return False 

def bCassandraServiceRunning(box,host):
         try:
           #print 'cqlsh '+z+' '+str(x['cassandra-port'])
           return_code=os.system('cqlsh '+host+' '+str(box['cassandra-port']+'>/dev/null'))
         except:
           print 'connection cannot be established on '+host+' on port '+str(box['cassandra-port'])
           pass
         else:
           if(return_code!=32512):
              print 'connection is established on '+host+'  on port '+str(box['cassandra-port'])
              return True
           else:
              return False
              # print 'connection cannot be established on '+z+' on port '+str(x['cassandra-port'])

  


def __main__():
   systemCheck()
   if(args.proxy_name==None):
      try:
        file_desc=open(args.yaml,'r')
        yaml_loader=yaml.load(file_desc)
        hosts_dic=yaml_loader['proxies']
        counter=1
        list_of_hosts=[]
        print 'Please select a hostname:'
        for host in hosts_dic:
          print str(counter)+'. '+host
          counter+=1
          list_of_hosts.append(host)
        result=False
        while(result!=True):
          try:
            choice=int(raw_input('Enter your choice: '))
          except:
            print 'Try again.please enter only integer value of your corresponding choice:'    
            continue 
          if (choice>counter-1 or choice<0):
            print 'Try again.please enter only integer value of your corresponding choice:'
          else:
            result=True                           
        val=hosts_dic[list_of_hosts[int(choice)-1]]['clusters']
        cons=0
        while(cons!=3):
          cons=0
          for box in val.values():
                   cluster=box['cassandra-hosts']
                   for host in cluster:
                     if(bCassandraServiceRunning(box,host)):
                          cons+=1  
        args.proxy_name=list_of_hosts[int(choice)-1]
        if( not bMetricServiceRunning()):
            print 'metric service is not running'        
            sys.exit(0)
              
      except IOError as e:
          print 'This filename does not exist.please check the filename and path to the file and re-enter '+str(e)
      
   print 'nohup /opt/reniac/software_proxy/rsds '+args.yaml+'  '+args.proxy_name
   
__main__()
