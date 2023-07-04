x=input('请输入一个不小于1000的整数:')
x=int(x)
print(x,'=',end='')
from math import *
while(0 in [x%i for i in range(2,int(sqrt(x))+1)]):
   for j in range(2,int(sqrt(x))+1):
       if x%j==0:
           print(j,'*',end='')
           x=x//j
           break
print(x)
    
   
    
