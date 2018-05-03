''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def remv(l,x,d,temp):
   #temp=[]
   #path=[x[0]]
   #print('hello')
   if x in l or [x[1],x[0]] in l:
     d[x[0]]+=1
     d[x[1]]+=1
     #print(str(x[0])+"  "+str(x[1]))
     return 1
   else:
      for y in l:
         #print(y)
         if x[0] in y:
            st=x[0] 
            if(x[0]==y[0]):
               x[0]=y[1]
            else:
               x[0]=y[0]
            #path.append(x[0])
            temp.append(y)
            l.remove(y)
            pat=remv(l,x,d,temp)
            if(pat==1):
                #print(st)
                d[st]+=1
                return 1
      return 0


def main():

 # Write code here 
    #n,m=list( int(x) for x in input().split() )
    n,m=list(int(x) for x in input().split())
    t=[]
    v=[]
    d={}
    temp=[]
    for i in range(1,n):
      t.append(list(int(x) for x in input().split() ))
      d[i]=0
    d[n]=0
    for i in range(m):
      v.append(list(int(x) for x in input().split() ))
    #print(v)
    #print("\n\n\n")
    for x in v: 
      #print(x)
      g=remv(t,x,d,temp)
      if(len(temp)>0):
         for y in temp:
           t.append(y)
         #t=list(set(t))
    print(max(d.values()))
    
main()    

