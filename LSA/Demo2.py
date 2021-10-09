import os
import re
from gensim import corpora, models
from gensim.similarities import Similarity

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
model = models.LsiModel(corpus, id2word=dictionary, num_topics=3)

vectorized_corpus = model[corpus]

print(list(vectorized_corpus))






# 测试数据
test_data = ['很多城市的污水防治没有完全落实，存在很多的污水防治问题']
test_cut = jieba.cut(test_data)
test_corpus = [dictionary.doc2bow(test_data)]

test_result = model[test_corpus]



from gensim.test.utils import common_corpus, common_dictionary, get_tmpfile
from gensim.models import LsiModel
list(common_dictionary)
model = LsiModel(common_corpus[:3], id2word=common_dictionary)  # train model
vector = model[common_corpus[4]]  # apply model to BoW document
model.add_documents(common_corpus[4:])  # update model with new documents
tmp_fname = get_tmpfile("lsi.model")
model.save(tmp_fname)  # save model
loaded_model = LsiModel.load(tmp_fname)  # load model







