#!/usr/bin/env python
import argparse
import sys
from RGitFramework import RGitFramework
import os
import yaml   
import urllib 
import ConfigParser as cp
import signal
import time

#/opt/reniac/software_proxy/multi.yaml
parser = argparse.ArgumentParser()
parser.add_argument('--yaml', default='test.yaml',help='Specify --yaml .yaml file path')
parser.add_argument('--proxy_name',help='Specify --proxy_name proxy ')
args = parser.parse_args()
#print args.conf,args.proxy_name


def conf_initiator():
   config = cp.ConfigParser()
   config.read('conf/conf.conf') 
   return "http://"+config.get('section','ip_address')+":"+config.get('section','port')


def bMetricServiceRunning():
   conn=urllib.urlopen(conf_initiator()) 
   if conn.getcode()==200:  
     return True
   else:
     return False 

def bCassandraServiceRunning(box,host,cassandra_port):
         try:
           #print 'cqlsh '+z+' '+str(x['cassandra-port'])
           return_code=rfobj.runme('cqlsh '+host+' '+cassandra_port+' > /dev/null')
         except:
           print 'connection cannot be established on '+host+' on port '+cassandra_port
           pass
         else:
           if(return_code!=32512):
              print 'connection is established on '+host+'  on port '+cassandra_port
              return True
           else:
              return False
              # print 'connection cannot be established on '+z+' on port '+str(x['cassandra-port'])


def handler (signum,frame) :
   sys.exit(0)

def check_reniac_system(rfobj,ipaddress, port,reniac_system_config,CQLSH_CMD):
    # check for python 2.7.x if not give the error message and exit.
    # metric services and cassandra services
    #stat
    pass        


def __main__():
   rfobj = RGitFramework()
   signal.signal(signal.SIGINT, handler)

   if not bMetricServiceRunning():
       print "Metric Service to be up and running - the system check has found it to not to be running. Please check it manually - exiting the setup."
       sys.exit()

   if(args.proxy_name==None):
      try:
        file_desc=open(args.yaml,'r')
        yaml_loader=yaml.load(file_desc)
        hosts_dic=yaml_loader['proxies']
        counter=1
        list_of_hosts=[]
        print '0. exit'
        print 'Please select a hostname:'
        for host in hosts_dic:
          print str(counter)+'. '+host
          counter+=1
          list_of_hosts.append(host)
        if(len(list_of_hosts)==1):
          val=hosts_dic[list_of_hosts[0]]['clusters']
        else:
          result=False  
          while(result!=True):
            try:
              choice=int(raw_input('Enter your choice: '))
            except ValueError:
              print 'Try again.please enter only integer value of your corresponding choice:'    
              continue 
            if (choice>counter-1 or choice<0):
              print 'Try again.please enter only integer value of your corresponding choice:'
            else:
              if(choice==0):
                 sys.exit(0)
              result=True                           
          val=hosts_dic[list_of_hosts[int(choice)-1]]['clusters']
        cons=0
        while(cons!=3):
          time.sleep(5)
          cons=0
          for box in val.values():
                   cluster=box['cassandra-hosts']
                   for host in cluster:
                     if(bCassandraServiceRunning(box,host,str(box['cassandra-port']))):
                          cons+=1  
        args.proxy_name=list_of_hosts[int(choice)-1]
        #if( not bMetricServiceRunning()):
        #    print 'metric service is not running'        
         #   sys.exit(0)
          
        
      except IOError as e:
          print 'This filename does not exist.please check the filename and path to the file and re-enter '+str(e)
     
   print 'nohup /opt/reniac/software_proxy/rsds '+args.yaml+'  '+args.proxy_name
   rfobj.runme('nohup /opt/reniac/software_proxy/rsds '+args.yaml+'  '+args.proxy_name)
   print rfobj.read_logs()
   print rfobj.error_logs()
   
__main__()
