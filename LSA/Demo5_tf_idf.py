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



print('=================dictinary=============')
print('词ID到这个词在多少篇文档数的映射(dfs):',dictionary.dfs)  # {单词id，在多少文档中出现}
print('词到id编码的映射(token2id):',dictionary.token2id)  # {词:id}
print('id编码到词的映射(id2token):',dictionary.id2token)
print('处理的文档数(num_docs):',dictionary.num_docs)
print('没有去重词条总数(num_pos):',dictionary.num_pos)
print('对文档内去重后的词条总数，文档间相同词不去重，只要记录BOW矩阵的非零元素个数(num_nnz):',dictionary.num_nnz)


# 一个词语在一篇文章中出现次数越多, 同时在所有文档中出现次数越少, 越能够代表该文章.
# TF) 指的是某一个给定的词语在该文件中出现的次数
# IDF) IDF的主要思想是：如果包含词条t的文档越少, IDF越大、
# TF-IDF倾向于过滤掉常见的词语，保留重要的词语。

model_tfidf = models.TfidfModel(corpus)
vector = model_tfidf[corpus[0]]
print(vector)
print(model_tfidf)


print('原词袋表示：')
for c in corpus:
    print(c)

corpus_tfidf = model_tfidf[corpus]
print(corpus_tfidf)
print(corpus_tfidf.corpus)

import numpy as np
corpus_tfidf_corpus = np.array(corpus_tfidf.corpus)


# 如果两个词多次出现在同一文档中，则这两个词在语义上具有相似性
# 矩阵元素代表该词在该文档中出现的次数
model_lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=3)
topics = model_lsi.get_topics()

self_topics = model_lsi.num_topics

model_lsi.print_topics(num_words=100)  # Get the most significant topics (alias for show_topics() method).
model_lsi.show_topics(num_words=10)


corpus_lsi = model_lsi[corpus]
for doc in corpus_lsi:
    print(doc)






