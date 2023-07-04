def myfilter(func,seq):
    for i in seq:
        if func(i)==True:
            yield i
if __name__=='__main__':
    seq=['foo','x41','?!','***']
    print(list(myfilter(str.isalnum,seq)))
