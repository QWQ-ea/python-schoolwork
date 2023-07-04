import collections
import re
with open('words.txt','r') as words:
 word=words.read()
 word=re.split('\n',word)
 word=collections.Counter(word)
 with open('output.txt','w') as output:
  output.writelines(str(word))
