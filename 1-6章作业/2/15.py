from random import *
a=[]
b={}
for i in range(1000):
     a.append(randint(0,100))
     b[a[i]]=b.get(a[i],0)+1
print(a,b,sep='\n')
      
