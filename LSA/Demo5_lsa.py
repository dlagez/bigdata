import os
import re
from gensim import corpora, models


# 小曾老师的数据，10/25发来的
# 判断属于哪一类主图
dir = '/Users/roczhang/Downloads/data_29/'

# 1.读取文件夹里面的文件
files = os.listdir(dir)
strs = []
for file in files:
    with open(dir+file, 'r') as file_to_read:
        temp = ''
        while True:
            lines = file_to_read.readline()  # 整行读取
            if not lines:  # 如果读到txt文件结尾了，读下一个文件
                break
            # lines = lines.strip('\n')  # 去掉文件结尾的换行符号
            lines = re.sub('[^\u4e00-\u9fa5]+', '', lines)  # 只保留汉字
            if len(lines) == 0:  # 如果读到空行，不记录
                continue
            temp = temp + lines
        strs.append(temp)
print(len(strs))



import jieba

strs_word = []
# 分词
for str in strs:
    temp = jieba.cut(str, use_paddle=True)
    strs_word.append(list(temp))
print(strs_word)

# 生成字段和向量语料
dictionary = corpora.Dictionary(strs_word)
# print("dictionary: " + str(dictionary))

corpus = [dictionary.doc2bow(text) for text in strs_word]
print(corpus)









