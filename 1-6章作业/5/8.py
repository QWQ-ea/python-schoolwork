def calculator(a):
    import re
    x=(len(re.findall('[a-z]', a)),len(re.findall('[A-Z]',a)),len(re.findall(r'\d',a)),len(re.findall('[^a-zA-z0-9]',a)))
    return x
if __name__=='__main__':
    a=input('请输入一个字符串:')
    b=['小写','大写','数字','其他']
    print(calculator(a))
    print(dict(zip(b,calculator(a))))
