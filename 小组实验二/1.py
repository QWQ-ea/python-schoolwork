def digui(k):
    m=1
    for i in range(1,k+1):
        m*=i
    return m
def qiouhe(k):
    return (digui(4*k)*(1103+26390*k))/((digui(k)**4)*(396**(4*k)))
x=int(input('请输入k:'))
y=0
for i in range(x+1):
    y=y+qiouhe(i)
pi=9801/(2*(2**0.5)*y)
print(pi)
