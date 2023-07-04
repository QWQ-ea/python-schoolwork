with open('words.txt','r') as f:
    wordlist = set([word.strip() for word in f.readlines()])
    #strip()去除字符串前后空格和换行符
# print(wordlist)
reverse = set()
#无序集合，不重复

for word in wordlist:
    if word[::-1] in wordlist and word != word[::-1]:  #[::-1]返回逆序字符串
        # x[start:stop:step] -1--> stop to start
        reverse.add((word,word[::-1]))

for i in reverse:
    print(i[0], i[1])
