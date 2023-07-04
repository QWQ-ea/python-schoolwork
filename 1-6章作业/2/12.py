data=['aabb','bcbcbc','aaaabbb','aabbcc']
for i in data:
    a={}
    for j in i:
        a[j]=a.get(j,0)+1
    if max(a.values())<=len(i)//2:
        print(i,end=',')
