import re
def count_keywords_frequency(file_path, keywords):
    # 读入文件内容
    with open(file_path,"r") as f:
        content = f.read()
    # 将大写字母转换成小写字母
    content = content.lower()
    # 初始化关键词出现次数的字典
    keywords_count = {}
    for keyword in keywords:
        keywords_count[keyword] = 0
    
    # 统计包含关键词的单词出现的次数
    pattern = re.compile(r'\b[a-zA-Z]+\b')
    words = pattern.findall(content)
    for word in words:
        if word in keywords_count:
            keywords_count[word] += 1

    # 计算关键词出现的频率
    total = sum(keywords_count.values())
    keywords_frequency = {}
    for keyword, count in keywords_count.items():
        if total > 0:
            frequency = count / total
        else:
            frequency = 0
        keywords_frequency[keyword] = frequency
    
    return keywords_frequency

keywords = ["apple", "banana", "na","ou"]
frequency = count_keywords_frequency("wenben2.txt", keywords)
print(frequency)
