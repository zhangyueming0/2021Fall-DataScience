# 这是针对含通知书的情况的处理，因本次实验文书样本均为裁定书，故不采用
from __future__ import unicode_literals
import sys
import jieba
import jieba.posseg as psg
import jieba.analyse
import json
import re;

sys.path.append("../")

jieba.load_userdict("src/main/resources/static/python/dict.txt")
jieba.load_userdict("src/main/resources/static/python/court.txt")
jieba.load_userdict("src/main/resources/static/python/charge.txt")

def stopwordslist(list):
    #去停用词
    res = []
    stopwords = [line.strip() for line in open('src/main/resources/static/python/stop.txt', encoding='UTF-8').readlines()]
    for word in list:
        if word not in stopwords:
            if word != '\t':
                res.append(word)
    return res


def lastG(str):
    countStr = str.count('罪')
    # 第一个指定字符的处理方法
    indexKey = str.find('罪')
    while countStr > 1:
        str_new = str[indexKey + 1:len(str) + 1]
        if str_new.find('、') < 0:
            break
        if str_new.find('被告人') >= 0:
            break
        indexKey = str_new.find('罪') + indexKey + 1
        countStr -= 1
    return indexKey


def rulingAndCourtVerdict(text):   #刑事裁定书
    res = text
    dictionary = {}
    dictionary['当事人'] = stopwordslist(jieba.analyse.extract_tags(res, allowPOS=('nr',)))
    temp = res.split('，')
    for i in range(len(temp)):
        if len(temp[i]) == 1:
            dictionary['性别'] = temp[i]
        if temp[i].find('族') >= 0:
            dictionary['民族'] = temp[i]
            break

    # 法院 指控被告人 犯 罪
    cause = []
    for j in temp:
        if j.find('指控被告人') >= 0:
            cause.append(j[j.index('犯') + 1:lastG(j) + 1])
            countFan = j.count('犯')
            indexKey = lastG(j) + 1
            while countFan > 1:
                str_new = j[indexKey + 1:len(j) + 1]
                if str_new.find('、') == 0:
                    break
                indexKey = str_new.find('犯') + indexKey + 1
                countFan -= 1
                cause.append(str_new[str_new.index('犯') + 1:lastG(str_new) + 1])
            break
    refer = jieba.analyse.extract_tags(res, allowPOS=('i',))
    dictionary['案由'] = cause

    # 出生地
    for n in range(len(temp)):
        k = temp[n]
        if k.find('出生于') >= 0:
            dictionary['地名'] = k[k.index('出生于') + 3:]
            break
        if k.find('出生') >= 0 & k.find('于') == 0:
            dictionary['地名'] = temp[n + 1][:temp[n + 1].index('人')]

    # 法院
    tempCourt = jieba.analyse.extract_tags(res, allowPOS=('nt',))
    courMat = []
    for x in tempCourt:
        if x.find('法院') >= 0:
            courMat.append(x)
    dictionary['相关法院'] = courMat

    with open('ouput.json', 'w') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=True, )

    return(dictionary)


def courtNotice(text):  #通知书
    res = text
    dictionary = {}
    dictionary['当事人'] = stopwordslist(jieba.analyse.extract_tags(res, allowPOS=('nr',)))
    temp = res.split('，')
    string = temp[0][temp[0].index('：')+1:]
    # 法院 指控被告人 犯 罪
    cause = []

    dictionary['案由'] = jieba.analyse.extract_tags(res, allowPOS=('i',))

    # 法院
    tempCourt = jieba.analyse.extract_tags(res, allowPOS=('nt',))
    courMat = []
    for x in tempCourt:
        if x.find('法院') >= 0:
            courMat.append(x)
    dictionary['相关法院'] = courMat

    with open('src/main/resources/templates/keyword.json', 'w') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=True, )
    return(dictionary)


def keyWord(text):
    if text[13:].find('调解书') >= 0:
        print(3)
        return "以调解方式结案"
    elif text[13:].find('通 知 书') >= 0:
        print(5)
        return courtNotice(text)
    else:
        return rulingAndCourtVerdict(text)

# 当事人，性别，民族，出生地，案由，相关法院


if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        text = sys.argv[i]
        text1 = keyWord(text)
        print(text1)