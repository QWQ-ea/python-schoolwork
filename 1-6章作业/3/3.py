x=input('请输入年份:')
x=int(x)
if (x%400==0)or(x%4==0 and x%10!=0):
    print('Yes')
else:
    print('No')
