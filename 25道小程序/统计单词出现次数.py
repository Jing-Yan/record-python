# -*- coding:utf-8 -*-

"""
任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
import re


def word_counter(filename):
    with open(filename, 'r') as f:
        text = f.read()
    words = re.findall('out', text)

    # 统计单词次数
    count = {}

    for word in words:
        print word
        count.setdefault(word, 0)
        count[word] += 1
        print count[word]
    print count


if __name__ == '__main__':
    word_counter('English.txt')
