import sys
import yaml
import os
 
ot=open('test.yaml','r')
code=yaml.load(ot)
ts=code['proxies']
val=ts['rsds1']['clusters']
cdir=ts['rsds1']['paths']['cache-dir']

if (cdir== None or cdir== ''):
  if not os.path.exists('./cache'):
   try:
      os.makedirs('./cache')
   except OSError as e:
      print 'Unable to create directory : ' + str(e)
   else:
      print 'Directory is created '
  else:
     print 'Directory already exists please check.'
  cdir='./cache'

if os.access(cdir, os.W_OK):
  print 'cache direcotry has write permission'
else:
  print 'cache directory does not have write permission'
  sys.exit(0)

