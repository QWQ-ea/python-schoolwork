def mymap(func,*seqs):
    for args in zip(*seqs):
        yield func(*args)
if __name__=='__main__':
    a=['1','2','3']
    print(list(mymap(int,a)))
    
