def markfuemphasize(filename,n):
    ''' 将filename文本的n阶分析结果放入字典并返回字典'''
    file=open(filename,'r',encoding='UTF-8')
    words=file.read().split()
    d={}
    for i in range(len(words)-n):
        s=' '.join(words[i:i+n:1])
        if s in d:
            d[s].append(words[i+n])
        else:
            d[s]=[words[i+n]]
    return d

def markfumakefile(d,n,m):
    ''' 通过markfuemphasize()函数返回的字典生成随机的m个句子'''
    import random
    firstword=random.choice(list(d))
    while firstword[0].islower():
        firstword=random.choice(list(d))
    chain=firstword.split()
    l=0
    #用l记录已生成的句子数
    for i in chain:
        if i[-1] in ('.','。','!','?'):
            l+=1
    while l<m:
      words=chain[-n:-1:1]
      #这里共有n-1个元素
      words.append(chain[-1])
      #chain[-1]为chain中最后一个元素
      words=' '.join(words)
      word=random.choice(d[words])
      chain.append(word)
      if word[-1] in ('.','?','!','。'):
            l+=1
    mphrase=' '.join(chain)
    return mphrase

if __name__=='__main__':
    import time
    start=time.time()
    d1=markfuemphasize('emma.txt',35)
    end = time.time()
    print(end - start,end='\n')
    start = time.time()
    mphrase1=markfumakefile(d1,35,10)
    end=time.time()
    print(end-start,end='\n')
    print(mphrase1, end='\n')
    start=time.time()
    d2=markfuemphasize('whitefang.txt',35)
    end = time.time()
    print(end - start, end='\n')
    start = time.time()
    mphrase2=markfumakefile(d2,35,10)
    end=time.time()
    print(end - start,end='\n')
    print(mphrase2,end='\n')

