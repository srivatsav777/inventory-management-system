#!/usr/bin/env python
import argparse
import ConfigParser as cp
import sys
#from RGitFramework import RGitFramework
import os
import yaml   
import signal
import urllib

def handler(signum, frame):
    print "\nReceive ^c singal - exiting the setup"
    sys.exit(1)
 

parser = argparse.ArgumentParser()
parser.add_argument('--yaml', default='/opt/reniac/software_proxy/multi.yaml',help='Specify --yaml .yaml file path')
parser.add_argument('--proxy_name',help='Specify --proxy_name proxy ')
args = parser.parse_args()
#print args.conf,args.proxy_name


def bCassandraRunning(rfobj, ipaddress, port,CQLSH_CMD):
    rfobj.runme(CQLSH_CMD + " " + ipaddress + " " + port + " -e help ")
    #print (CQLSH_CMD + " " + ipaddress + " " + port + " -e help ")
    conn=urllib.urlopen("http://"+ipaddress+":"+port)
    print "Checking connection with cassandra running at "+ ipaddress + " " + port
    if rfobj.read_logs():
            return True
    else :
            return False

def bMetricServiceRunning () :
    return True


def check_reniac_system(rfobj,ipaddress, port,reniac_system_config,CQLSH_CMD):
    # check for python 2.7.x if not give the error message and exit.
    # metric services and cassandra services
    #stat
    pass        

def getUrl(conf='/opt/reniac/metrics_service/conf/metrics_service.conf'):
  config = cp.ConfigParser()
  config.read(conf)
  ip_address=config.get('metrics_service','ip_address')
  port=config.get('metrics_service','port')
  return "http://"+str(ip_address)+":"+str(port)

def bMetricServiceRunning():
  try :
      conn=urllib.urlopen(getUrl())
      if conn.getcode()==200:  
        return True
      else:
        return False 
  except:
      print "Service is not up and running - please start the service and try again. The ip and port valuses are being taken from /opt/reniac/metrics_service/conf/metrics_service.conf"

def __main__():
   signal.signal(signal.SIGINT,handler)
   #rfobj = RGitFramework()
   
   if not bMetricServiceRunning():
       print "Metric Service is a mandatory service before software proxy can be started  - the system check has found it not to be running. Please check it manually - exiting the setup."
       sys.exit(1)
   else:
        print "The metrics services is up and running at " + getUrl() +" . Going to the next step"

   if(args.proxy_name==None):
      try:
        file_desc=open(args.yaml,'r')
        yaml_loader=yaml.load(file_desc)
        hosts_dic=yaml_loader['proxies']
        counter=1
        list_of_hosts=[]
        for host in hosts_dic:
          list_of_hosts.append(host)
        if len(list_of_hosts) < 1:
            print "Looks like problem in the yaml file as there is so section for the proxy. Exiting the setup - please contact reniac."
            sys.exit()
        if len(list_of_hosts) > 1:
            print 'Please select a hostname:'
            counter=1
            for host in hosts_dic:
                print str(counter)+'. '+host
                counter+=1
            result=False
        
            while(result!=True):
              try:
                choice=int(raw_input('Enter your choice for the proxy or 0 to exit: '))
                if choice == 0:
                    print "Exiting the setup."
                    sys.exit(1)
              except ValueError:
                print 'Try again.please enter only integer value of your corresponding choice:'    
                continue 
              if (choice>counter-1 or choice<0):
                print 'Try again.please enter only integer value of your corresponding choice:'
              else:
                result=True                           
            val=hosts_dic[list_of_hosts[int(choice)-1]]['clusters']
        else:
            val=hosts_dic[list_of_hosts[0]]['clusters']
        cons=0
        for y, x in val.iteritems():
                   t=x['cassandra-hosts']
                   isClusterLive=False
                   for z in t:
                      port=str(x['cassandra-port'])
                      ipaddress=z
                      if bCassandraRunning(rfobj, ipaddress, port,"cqlsh"):
                          isClusterLive=True
                          break; 
                   if isClusterLive == False:
                       print "The cluster ",y, t , " does not have any live connection - exiting the setup"
                       sys.exit() 
        args.proxy_name=list_of_hosts[int(choice)-1]
      except IOError as e:
          print 'This filename does not exist.please check the filename and path to the file and re-enter '+str(e)
     
   print 'nohup /opt/reniac/software_proxy/rsds '+args.yaml+'  '+args.proxy_name
   #rfobj.runme('nohup /opt/reniac/software_proxy/rsds '+args.yaml+'  '+args.proxy_name + " 2>&1 | tee /opt/reniac/logs/software_proxy.log & ")
   print rfobj.read_logs()
   print rfobj.error_logs()
   
__main__()
