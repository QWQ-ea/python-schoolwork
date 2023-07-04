import re
a=re.compile(r'\b[a-zA-z]{3}\b')
x=input('请输入:')
print(a.findall(x))
