time=input("请输入一个时间如(12:59:59) :")
list=time.split(":")
list=[int(x) for x in list]

hour=list[0]
min=list[1]
sec=list[2]

if(hour<0 or min<0 or sec<0):
   print('输入时间不合理，请重新输入。')
elif(hour>24 or min>=60 or sec>=60):
   print('输入时间不合理，请重新输入。')
elif sec==59:
    min +=1
    sec = 0
    if min==60:
        min=0
        hour +=1
        if hour==24:
            hour=0
    print('下一秒的时间为%02d:%02d:%02d'%(hour,min,sec))
else:
    sec +=1
    print('下一秒的时间为%02d:%02d:%02d'%(hour,min,sec))
