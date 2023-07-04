def is_reducible(word, word_dict, reducible_dict):
    # 判断一个单词是否可缩减
    if word in reducible_dict:
        return reducible_dict[word]
    if word in ['i', 'a']:
        reducible_dict[word] = True
        return True
    # 遍历单词中的每个字母，在单词列表中查找子单词是否可缩减
    for i in range(len(word)):
        child_word = word[:i] + word[i+1:]
        if child_word in word_dict and is_reducible(child_word, word_dict, reducible_dict):
            reducible_dict[word] = True
            return True
    reducible_dict[word] = False
    return False

def find_longest_reducible_word(word_list):
    # 在单词列表中查找最长可缩减单词
    word_dict = set(word_list)
    reducible_dict = {}
    longest_reducible_word = ''
    # 遍历所有单词，判断是否可缩减，更新最长可缩减单词
    for word in word_dict:
        if is_reducible(word, word_dict, reducible_dict):
            if len(word) > len(longest_reducible_word):
                longest_reducible_word = word
    return longest_reducible_word

if __name__ == '__main__':
    with open('words.txt', 'r') as fin:
        word_list = [line.strip() for line in fin]
    longest_reducible_word = find_longest_reducible_word(word_list)
    print('The longest reducible word is:', longest_reducible_word)
