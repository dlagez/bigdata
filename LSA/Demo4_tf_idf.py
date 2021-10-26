import os
import re
from gensim import corpora, models
from gensim.similarities import Similarity
from gensim.test.utils import common_dictionary, common_corpus
import gensim.downloader as api
from gensim.corpora import Dictionary

# 小曾老师的数据，2016 里面有8个文本，提取里面的关键词
# 判断属于哪一类主图
dir = '/Users/roczhang/Downloads/2016/'

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

# 生成模型
# model = models.LsiModel(corpus, id2word=dictionary, num_topics=3)
# 判断一个文档的词频重要性，因为没有分开 分开操作 corpus = [dct.doc2bow(line) for line in dataset]
model = models.TfidfModel(corpus)
vector = model[corpus[0]]
print(vector)

print('=================dictinary=============')
print('词ID到这个词在多少篇文档数的映射(dfs):',dictionary.dfs)
print('词到id编码的映射(token2id):',dictionary.token2id)
print('id编码到词的映射(id2token):',dictionary.id2token)
print('处理的文档数(num_docs):',dictionary.num_docs)
print('没有去重词条总数(num_pos):',dictionary.num_pos)
print('对文档内去重后的词条总数，文档间相同词不去重，只要记录BOW矩阵的非零元素个数(num_nnz):',dictionary.num_nnz)

print('原词袋表示：')
for c in corpus:
    print(c)
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
print('转换整个语料库：')
for doc in corpus_tfidf:
    print(doc)







