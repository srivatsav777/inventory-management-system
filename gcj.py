import sys
sys.stdout.flush()
t=int(raw_input())
for i in range(t):
  n=int(input())
  digits=list(str(n))
  if(len(digits)==1):
     print('Case #'+str(i+1)+': '+str(n))  
  elif(sorted(digits)==digits):
    print('Case #'+str(i+1)+': '+str(n))
  elif(sorted(digits)[0]=='0' and sorted(digits)[-1]=='1'):
     print('Case #'+str(i+1)+': '+'9'*(len(digits)-1))
  elif('0' in digits):
     x=digits.index('0')
     if(int(digits[x-1])>1):
        digits[x-1]=str(int(digits[x-1])-1)
        digits[x:]=[str(9) for y in range(x,len(digits))]
        print('Case #'+str(i+1)+': '+''.join(digits))
     elif(int(digits[x-1])==1):
        print('Case #'+str(i+1)+': '+'9'*(len(digits)-1))
     else:
        t=n%10
        print('Case #'+str(i+1)+': '+str(n-t-1))
  else:
    t=n%10
    digits=list(str(n-t-1))  
    while(sorted(digits)!=digits):
     x=digits.index(sorted(digits)[0])
     digits[x-1]=str(int(digits[x-1])-1)
     digits[x:]=[str(9) for y in range(x,len(digits))]
    print('Case #'+str(i+1)+': '+''.join(digits))

