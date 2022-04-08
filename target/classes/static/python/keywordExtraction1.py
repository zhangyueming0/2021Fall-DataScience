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

def keyWord(text):
    res=text
    dictionary = {}
    dictionary['当事人'] = stopwordslist(jieba.analyse.extract_tags(res, allowPOS=('nr',)))
    temp = res.split('，')
    for i in range(10):
        if len(temp[i]) == 1:
            dictionary['性别'] = temp[i]
        if temp[i].find('族') >= 0:
            dictionary['民族'] = temp[i]
            break
    for j in temp:
        if j.find('指控被告人') >= 0:
            dictionary['案由'] = j[j.index('犯')+1:j.index('罪')+1]
            break
    dictionary['地名'] = stopwordslist(jieba.analyse.extract_tags(res, allowPOS=('ns',)))
    tempCourt = jieba.analyse.extract_tags(res, allowPOS=('nt',))
    courMat = []
    for x in tempCourt:
        if x.find('法院') >= 0:
            courMat.append(x)
    dictionary['相关法院'] = courMat
    with open('src/main/resources/templates/keyword.json', 'w',encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=True, )
    return(dictionary)
if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        text = sys.argv[i]
        text1 = keyWord(text)
        print(text1)




