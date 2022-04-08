from __future__ import print_function, unicode_literals
import sys

sys.path.append("../")

import jieba
import jieba.analyse
import json
import re
from optparse import OptionParser

import jieba.posseg as pseg
jieba.load_userdict("src/main/resources/static/python/dict.txt")
jieba.load_userdict("src/main/resources/static/python/court.txt")
def stopwordslist(list):
    #去停用词
    res = []
    stopwords = [line.strip() for line in open('src/main/resources/static/python/stop.txt', encoding='UTF-8').readlines()]
    for word in list:
        if word not in stopwords:
            if word != '\t':
                res.append(word)
    return(res)
def others(text):
    res=text
    dictionary = {}
    dictionary['名词'] = stopwordslist(jieba.analyse.extract_tags(res, allowPOS=('nr',)) + jieba.analyse.extract_tags(res, allowPOS=('ns',)) + jieba.analyse.extract_tags(res, allowPOS=('nz',)) + jieba.analyse.extract_tags(res, allowPOS=('n',)))
    dictionary['动词'] = stopwordslist(jieba.analyse.extract_tags(res, allowPOS=('v',)))
    dictionary['形容词'] = stopwordslist(jieba.analyse.extract_tags(res, allowPOS=('a',)))
    dictionary['时间词'] = stopwordslist(jieba.analyse.extract_tags(res, allowPOS=('t',)))
    with open('src/main/resources/templates/partsofspeech.json', 'w',encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=True, )

    return(dictionary)

if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        text = sys.argv[i]
        text1 = others(text)
        print(text1)



