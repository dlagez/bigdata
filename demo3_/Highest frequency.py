import os
import re
import jieba
from collections import Counter
from gensim import corpora, models

dir = '/Volumes/roczhang/WHPU/zen/政策文本txt/'

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

# 把所有文本分词，并放入strsList里面
strList = []
# 分词
for i in strs:
    temp = jieba.cut(i, use_paddle=True)
    strList.append(list(temp))
print(strList)
'的' in strList[0]

# 读取停用词
stopWordsFile = open('/Volumes/roczhang/WHPU/zen/词频图/停用词表.txt')
stopWords = [line.strip() for line in stopWordsFile.readlines()]

# 除去停用词
def CutWithStopWord(strList, stopWord):
    cutList = []
    for word in strList:
        if word not in stopWord and len(word) > 1:
            cutList.append(word)
    return cutList

# 功能：统计分词之后出现次数最多的N个词
# 输入参数
#       words：分词之后的词列表
#       N：出现次数最多的N个词
# 返回值
#       wordListNTop：出现次数最多的N个词及其出现的次数
def StatTopNWords(words, N):
    wordList = []
    wordList = Counter(words)  #统计每个词出现的次数
    wordListNTop = wordList.most_common(N)  #统计出现的次数最多的N个词及出现的次数
    return wordListNTop

# 将去除了停用词的词放入WordList里面
# WordList = CutWithStopWord(strList, stopWords)
WordList = []
for word in strList:
    if word not in stopWords:
        WordList.append(word)


# wordListNTop = StatTopNWords(WordList, 100) # 这个方法只能处理一位列表，不能处理二维列表
'的' in WordList[0]
'和' in WordList[0]
# 找出每篇文章频率最高的词
result = []
for i in WordList:
    temp = StatTopNWords(i, 100)
    result.append(temp)


# 将每个文件频率前100的数据写入文件
output = open('/Volumes/roczhang/WHPU/zen/result.txt', 'w')
for i in range(len(result)):
    output.write('第' + str(i) + '篇文章!' + '\n')  # 在每篇（每一行开始的时候做一个标记）
    for j in range(len(result[i])):
        # print(result[i][j])
        output.write(str(result[i][j]))  # 写入一行数据
        output.write(' ')
    output.write('\n\n')  # 每写完一行数据之后按两次回撤键
output.close()

# 将所有文件合并, 然后求频率最高的词
all_word = [i for item in WordList for i in item]
StatTopNWords(all_word, 100)

test = ['的', 'aaa']
for word in test:
    if word not in stopWords and len(word) > 1:
        print(word)
