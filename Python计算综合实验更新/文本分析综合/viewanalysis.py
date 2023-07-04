from matplotlib import pyplot as plt
import matplotlib
matplotlib.rc('font',family='YouYuan')
# 读取统计结果文件
virtual_word_freq = {}
real_word_freq = {}

with open('word_freq.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if i > 0 and i<11:
            for word_freq in line.split():
                word, freq = word_freq.split(':')
                virtual_word_freq[word] = eval(freq)
        elif i > 12 and i <22:
            for word_freq in line.split():
                word, freq = word_freq.split(':')
                real_word_freq[word] = eval(freq)

# 绘制柱状图
plt.figure()
plt.bar(list(virtual_word_freq.keys()), list(virtual_word_freq.values()),align='center')
plt.title('文本虚词频率统计')
plt.xlabel('虚词')
plt.ylabel('出现频率')
plt.show()
plt.bar(list(real_word_freq.keys()), list(real_word_freq.values()),align='center')
plt.title('文本实词频率统计')
plt.xlabel('实词')
plt.ylabel('出现频率')
plt.show()


