import re
st = input("请输入：")
pattern=re.compile(r'\bi\b')
st=pattern.sub('I',st)
print(st)
