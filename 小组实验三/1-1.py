def ack(m,n):
    if m==0:
        y=n+1
        return y
    elif m>0 and n==0:
        y=ack(m-1,1)
        return y
    elif m>0 and n>0:
        y=ack(m-1,ack(m,n-1))
        return y

print('ack(3,4)的值为：',ack(4,5))

    
