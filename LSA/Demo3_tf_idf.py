import os
import re
from gensim import corpora, models
from gensim.similarities import Similarity

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
print(strs)

from snownlp import SnowNLP

for str in strs:
    s = SnowNLP(str)
    # print(s.keywords(4))
    print(s.tf)
