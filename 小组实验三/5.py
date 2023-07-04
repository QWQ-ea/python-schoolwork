import re

'''
    编写函数 rotateword,接收一个字符串 strsrc 以及一个整数 n 作为参数，
    返回新字符串 strdes,其各个字母是 strsrc 中对应位置各个字母在字母表中“轮
    转”n 字符后得到的编码。
'''


#def rotateword(strsrc,n):
#    import string as s
#    lower=s.ascii_lowercase[n:]+s.ascii_lowercase[:n]
#    upper=s.ascii_uppercase[n:]+s.ascii_uppercase[:n]
#    table=''.maketrans(s.ascii_letters,lower+upper)
#    strdes=strsrc.translate(table)
#    return strdes


def rotateword(strsrc, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # 单词表
    regex = re.compile('[a-zA-Z]')
    strdes = ''
    for char in strsrc:
        if regex.match(char):
            is_upper = char.isupper()   #判断是否是大写
            char = char.lower()
            idx = (alphabet.index(char) + n) % 26   #轮转
            rotated_char = alphabet[idx]
            if is_upper:
                rotated_char = rotated_char.upper() #若为大写，重新大写
            strdes += rotated_char
        else:
            strdes += char
    return strdes

'''
    编写函数 avoids,接收一个单词和一个含有禁止字母的字符串,判断
    该单词是否含有禁止字母。
'''

def avoids(word, forbidden):
    pattern = "[" + forbidden + "]" # 一组字符 [amk] 匹配 'a'，'m'或'k'
    if re.search(pattern, word):
        return True # 含有禁止字母
    return False # 不含禁止字母

'''
    编写函数 useonly,接收一个单词和一个含有允许字母的字符串,判断
    单词是否仅仅由允许字母组成。
'''

def useonly(word, allow):
    regex = re.compile('^[' + allow + ']+$') # ^ 和 $ 限制开头和结尾
    return bool(regex.match(word))

'''
    编写函数 useall,接收一个单词和一个含有需要字母的字符串,判断该
    单词是否包含了所有需要字母至少一个,并输出 words.txt 中使用了所有元音字
    母 aeiou 的单词。
'''

def useall(word, allow):
    for c in allow:
        if not re.search(c, word):
            return False
    return True

def aeiou_words():
    list = set()
    with open('words.txt', 'r') as file:
        for word in file:
            if re.search('[aeiou]', word) and useall(word.strip(), 'aeiou'):
                # search是否包含任何元音字母
                list.add(word.strip())
    print(len(list),end='\n')

'''
    编写函数 hasnoe,判断一个英语单词是否包含字母 e,并计算 words.txt
    中不含 e 的单词在整个字母表中的百分比。
'''

def hasnoe(char):
    return not re.search('e', char)

def noe_words():
    with open('words.txt', 'r') as file:
        sum = 0
        no_e = 0
        for word in file:
            sum += 1
            if hasnoe(word.strip()):
                no_e += 1
        percentage = (no_e / sum) * 100
        print("百分比为: {:.2f}%".format(percentage),no_e,end='\n')
    

'''
    编写函数 isabecedarian,判断一个英语单词中的字母是否符合字母表序,
    并且输出 words.txt 中所有这样的单词
'''

def isabecedarian(word):
    return bool(re.match(r'^a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*$', word))# re* 匹配0个或多个

def sort_words():
    list = set()
    with open('words.txt', 'r') as file:
        for word in file:
            if isabecedarian(word.strip()):
                list.add(word.strip())
    print(len(list),end='\n')

if __name__ == '__main__':
    # 1
    assert rotateword('Hello, World!', 5) == 'Mjqqt, Btwqi!'
    assert rotateword('xyz123', 3) == 'abc123'
    assert rotateword('', 5) == ''
    # 2
    assert avoids("hello", "xyz") == False
    assert avoids("world", "xyz") == False
    assert avoids("Python", "pt") == True
    assert avoids("Java", "pt") == False
    # 3
    assert useonly('hello', 'helo') == True # 仅由h,e,l,o组成
    assert useonly('world', 'helo') == False
    assert useonly('hello!!', '!') == False
    # 4
    assert useall('hello!!', '!') == True
    aeiou_words()
    # 5
    assert hasnoe('hello!!') == False   #存在e
    assert hasnoe('12ioo') == True      #不存在e
    noe_words()
    # 6
    assert isabecedarian('a') == True
    assert isabecedarian('bdf') == True
    assert isabecedarian('eg') == True
    assert isabecedarian('ahy') == True
    assert isabecedarian('zxy') == False
    sort_words()
    print("测试通过")