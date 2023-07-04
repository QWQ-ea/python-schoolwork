import re
# 构建实现该功能的函数
def count_words(file_path):
    # 读入文件内容,存储到变量content中
    with open(file_path,"r") as f:
        content = f.read()
    # 将大写字母转换成小写字母
    content = content.lower()
    # 初始化一个空字典来存储各个单词的出现次数
    words_count = {}
    # 使用正则表达式提取文本中的英文单词
    pattern = re.compile(r'\b[a-zA-Z]+\b')
    words = pattern.findall(content)
    # 遍历列表，逐个统计
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1    
    return words_count

# 调用函数
words_count = count_words("wenben.txt")
print(words_count)
