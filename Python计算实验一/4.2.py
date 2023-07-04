import re
import collections
word=input('请输入要查找的单词:')
word=list(map(str,word.split(' ')))
with open('words.txt','r') as words:
    lines=words.read()
    lines=re.split('\n',lines)
    lines=collections.Counter(lines)
    for i in range(len(word)):
        print(str(word[i]),lines[str(word[i])],sep=':',end='\n')
    
