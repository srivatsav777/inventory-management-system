import re

l=["Op rate:16,301 op/s  [READ: 16,301 op/s]",
"Partition rate:16,301 pk/s  [READ: 16,301 pk/s]",
"Row rate:16,301 row/s [READ: 16,301 row/s]",
"Latency mean:0.2 ms [READ: 0.2 ms]",
"Latency median:0.2 ms [READ: 0.2 ms]",
"Latency 95th percentile:0.2 ms [READ: 0.2 ms]",
"Latency 99th percentile:0.3 ms [READ: 0.3 ms]",
"Latency 99.9th percentile:3.1 ms [READ: 3.1 ms]",
"Latency max:57.6 ms [READ: 57.6 ms]",
"Total partitions:1,000,000 [READ: 1,000,000]",
"Total errors:0 [READ: 0]",
"Total GC count:0",
"Total GC memory:0.000 KiB",
"Total GC time:0.0 seconds",
"Avg GC time:NaN ms",
"StdDev GC time:0.0 ms",
"Total operation time:00:01:01"
]

m=["Op rate:16,301 op/s  [READ: 16,301 op/s]",
"Partition rate:16,301 pk/s  [READ: 16,301 pk/s]",
"Row rate:16,301 row/s [READ: 16,301 row/s]",
"Latency mean:0.2 ms [READ: 0.2 ms]",
"Latency median:0.2 ms [READ: 0.2 ms]",
"Latency 95th percentile:0.2 ms [READ: 0.2 ms]",
"Latency 99th percentile:0.3 ms [READ: 0.3 ms]",
"Latency 99.9th percentile:3.1 ms [READ: 3.1 ms]",
"Latency max:57.6 ms [READ: 57.6 ms]",
"Total partitions:1,000,000 [READ: 1,000,000]",
"Total errors:0 [READ: 0]",
"Total GC count:0",
"Total GC memory:0.000 KiB",
"Total GC time:0.0 seconds",
"Avg GC time:NaN m",
"StdDev GC time:0.0 ms",
"Total operation time:00:01:01"
]



print 'Parameters                |         Baseline                  |            Proxy_metrics          |      Differrence     '
fi=open("res.txt","w")
fi.write('Parameters                |         Baseline                  |            Proxy_metrics          |      Differrence     \n')
for x,y in zip(l,m):
     p=x.split(":",1)
     q=y.split(":",1)
     t1=p[1].split("[")[0]
     unit=re.findall(r'[a-z]+\/*[a-z]',t1)
     unit="".join(unit)
     t2=q[1].split("[")[0]
     lis_of_int1=map(int, re.findall(r'\d+', t1))
     lis_of_int2=map(int, re.findall(r'\d+', t2))
     if(len(lis_of_int1)== 0 or len(lis_of_int2) == 0):
       diff=0
     else:
       m=int("".join(str(z) for z in lis_of_int1))
       n=int("".join(str(z) for z in lis_of_int2))
       diff=m-n
     print str(p[0])+"            |"+str(p[1])+"   |"+str(q[1])+"   |   "+(str(diff)+str(unit))
     fi.write(str(p[0])+"          |"+str(p[1])+"   |"+str(q[1])+"   |   "+(str(diff)+str(unit))+"\n")

