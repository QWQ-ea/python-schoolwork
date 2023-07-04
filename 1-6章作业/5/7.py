def isprime(x):
    '''判断一个数是否为素数'''
    if x>1:
         for i in range(2,int(x**0.5)+1):
             if x%i==0:
                 return True
    return False
if __name__=='__main__':
   x=int(input('请输入一个数:'))
   if isprime(x):
    print(x,'为素数',sep='')
   else:
    print(x,'不是素数',sep='')
