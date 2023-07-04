def Sum(a):   
    from functools import reduce
    return reduce(lambda x,y:x+y,a)
if __name__=='__main__':
    a=[1,2,3,4,5]
    b=(7,8,9,6)
    print(Sum(a))
    print(Sum(b))
