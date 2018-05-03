import json

sample={}
sample= json.load(open('tem.json'))

for s in sample.iteritems():
  print s

