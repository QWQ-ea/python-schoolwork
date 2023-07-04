import jieba
from collections import Counter

def word_frequency(text, word):
    words = jieba.lcut(text)
    counter = Counter(words)
    return counter[word]

with open('dreamofredmaison.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 分析前80回和后40回的文言虚实字词
virtual_words = ['之', '者', '而', '乎', '其', '也', '矣', '于', '之所以', '之所以然']
real_words = ['不', '无', '非', '未', '勿', '莫', '毋', '岂', '止', '不止']

virtual_word_freq = {}
real_word_freq = {}

for word in virtual_words:
    freq = word_frequency(text, word)
    virtual_word_freq[word] = freq

for word in real_words:
    freq = word_frequency(text, word)
    real_word_freq[word] = freq

# 将结果存入文件
with open('word_freq.txt', 'w', encoding='utf-8') as f:
    f.write('文言虚词词频：\n')
    for word, freq in virtual_word_freq.items():
        f.write(f'{word}:{freq}\n')
    f.write('\n')
    f.write('文言实词词频：\n')
    for word, freq in real_word_freq.items():
        f.write(f'{word}:{freq}\n')
