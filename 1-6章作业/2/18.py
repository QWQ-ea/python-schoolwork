from random import *
a=[randint(0,100) for i in range(20)]
print(sorted(a[:10]),sorted(a[10:20],reverse=True))
