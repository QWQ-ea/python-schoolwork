from random import *
a=[randint(0,100) for i in range(50)]
for i in a[:]:
    if i%2!=0:
        a.remove(i)
print(a)
