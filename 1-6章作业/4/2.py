import re
s = input('请输入一段英文:')
pattern=re.compile(r'\b\w+(I)\w+\b')
a=pattern.search(s)
print(a.span(2))

