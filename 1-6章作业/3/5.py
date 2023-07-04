from random import *
a=[randint(0,100) for i in range(20)]
print(sorted(a[::2],reverse=True))
