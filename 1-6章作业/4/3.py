import re
x=input('请输入:')
print(re.sub(r'(\b\w+) \1',r'\1',x))
