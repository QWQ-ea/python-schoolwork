x=input('请输入一个列表:')
a=[]
for i in range(1,len(x)-1):
    if x[i]!=',':
      a.append(int(x[i]))
x=input('请输入两个整数:')
b,c=map(int,x.split(','))
print([i for i in a[b:c+1]])


    
