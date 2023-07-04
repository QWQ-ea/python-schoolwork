x=input('请输入M和N:')
import re
x=list(map(int,re.split(' ',x)))
m,n=x[0],x[1]
print(m,n,end='\n')
import random
a={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
b=[[(y:=random.randint(1,12),random.randint(1,a[y])) for i in range(n)] for j in range(m)]
print(b)
q=0
for item in b:
    len1=len(item)
    len2=len(set(item))
    if len1!=len2:
        q=q+1
p=q/m
print(p)
