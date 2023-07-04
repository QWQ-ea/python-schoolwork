class myTime():
    def isvalid(self,h,m,s):
        if h not in range(0,24) or not isinstance(h,int):
            print('hour must be a number and be included in [0-23]')
            return False
        elif m not in range(0,60) or not isinstance(m,int):
             print('minute must be a number and be included in [0-59]')
             return False
        elif s not in range(0,60) or not isinstance(s,int):
             print('second must be a number and be included in [0-59]')
             return False
        return True
        
    def __init__(self,h=0,m=0,s=0):
        if self.isvalid(h,m,s):
            self.hour=h
            self.minute=m
            self.second=s
        else:
            return
    def __str__(self):
        return str(self.hour)+':'+str(self.minute)+':'+str(self.second)
    def __add__(self,n):
        m=myTime()
        m.hour=self.hour
        m.minute=self.minute
        m.second=self.second
        if isinstance(n,int):
            m.second+=n
            m.minute+=m.second//60
            m.second%=60
            m.hour+=m.minute//60
            m.minute%=60
            m.hour%=24
        elif isinstance(n,myTime):
            m.second+=n.second
            m.minute+=(m.second//60+n.minute)
            m.second%=60
            m.hour+=(m.minute//60+n.hour)
            m.minute%=60
            m.hour%=24
        return m
    def time2int(self):
        m=self.hour*3600+self.minute*60+self.second
        return m
    def printtime(self):
        print(self.hour,self.minute,self.second,sep=':')
    def isafter(self,m):
        if self.hour>m.hour:
            print('The latter precedes the former')
        elif self.hour<m.hour:
            print('The former precedes the latter')
        elif self.minute>m.minute:
            print('The latter precedes the former')
        elif self.minute<m.minute:
            print('The former precedes the latter')
        elif self.second>m.second:
            print('The latter precedes the former')
        elif self.second<m.second:
            print('The former precedes the latter')
    def increment(self,n):
        m=self+n
        m.printtime()
if __name__=='__main__':
 time1=myTime(0,0,0)
 time2=myTime(23,59,59)
 print('time1为:',time1,sep='')
 print('time2为:',end='')
 time2.printtime()
 time1.second=2
 print('time1+time2为:',time1+time2,sep='')
 print('time2对象转化为秒数为:',time2.time2int(),sep='')
 print('time2加两秒后为:',end='')
 time2.increment(2)
 print('比较time1和time2的先后',end=''),
 time1.isafter(time2)
