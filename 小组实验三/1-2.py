import random
def dedupe(list):
    seen = []
    for i in list:
        if i not in seen:
            seen.append(i)
    return seen
a = [random.randint(1,10) for i in range(20)]
print('原列表',a,'\n')
print('去重后',dedupe(a),'\n\n')

def dedupe(items,key=None):
    seen=set()
    for item in items:
        value=item if key is None else key(item) #不可哈希
        if value not in seen:
            yield item  #生成器保证顺序不变
            seen.add(value)

a=[
    {'a':1,'b':2,'c':3},
    {'a':1,'b':3,'c':3},
    {'a':1,'b':4,'c':3},
    {'a':1,'b':2,'c':3},
    {'a':1,'b':3,'c':3},
    {'a':1,'b':1,'c':3},

]
print('原字典',a,'\n')
print('去重后',list(dedupe(a,key=lambda d:(d['a'],d['b'],d['c']))))

