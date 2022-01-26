import jieba.analyse
import os
from collections import Counter
import json
# 取词 关键词 textrank 这个程序是将所有的文本提取关键词之后，再将每个文本的关键词进行对比，取交集。

# ref: https://blog.csdn.net/cdlwhm1217096231/article/details/94566936?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task%20%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%E2%80%94%20%E7%89%88%E6%9D%83%E5%A3%B0%E6%98%8E%EF%BC%9A%E6%9C%AC%E6%96%87%E4%B8%BACSDN%E5%8D%9A%E4%B8%BB%E3%80%8C%E7%AD%B1%E5%B0%8F%E9%BE%99%E3%80%8D%E7%9A%84%E5%8E%9F%E5%88%9B%E6%96%87%E7%AB%A0%EF%BC%8C%E9%81%B5%E5%BE%AACC%204.0%20BY-SA%E7%89%88%E6%9D%83%E5%8D%8F%E8%AE%AE%EF%BC%8C%E8%BD%AC%E8%BD%BD%E8%AF%B7%E9%99%84%E4%B8%8A%E5%8E%9F%E6%96%87%E5%87%BA%E5%A4%84%E9%93%BE%E6%8E%A5%E5%8F%8A%E6%9C%AC%E5%A3%B0%E6%98%8E%E3%80%82%20%E5%8E%9F%E6%96%87%E9%93%BE%E6%8E%A5%EF%BC%9Ahttps://blog.csdn.net/weixin_30253289/article/details/114715240
# stopwords = [line.strip() for line in
#              open(r'C:\roczhang\WHPU\zen\词频图\停用词表.txt',
#                   encoding='UTF-8').readlines()]
# # 将每个txt文件应用 textrank 提取关键词
# base_dir = r'C:\roczhang\WHPU\zen\data'
# target_dir = r'C:\roczhang\WHPU\zen\key'
# list_name = os.listdir(base_dir)
# for name in list_name:
#     with open(base_dir + '\\' + name, 'r', encoding='utf-8') as f:
#         content = f.read()
#         result = jieba.analyse.textrank(content, topK=350, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
#         file_name = name.split('.')[0]
#         with open(target_dir + '\\' + file_name + '-keywords' + '.txt', 'w', encoding='utf-8') as save_file:
#             for i in result:
#                 save_file.write(i + '\n')

# 取出交集，（只要某个关键词出现五次以上，就提取出来）

# 将所有关键词合并，取出不重复的关键词
merged = []
base_key_dir = r'C:\roczhang\WHPU\zen\key'
key_list = os.listdir(base_key_dir)
for key in key_list:
    with open(base_key_dir + '\\' + key, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            merged.append(line)
result = Counter(merged)
result_set = result.keys()
sorted_result = sorted(result.items(), key=lambda item: item[   1], reverse=True)

# sorted_result = sorted_result[:350]

with open(r'C:\roczhang\WHPU\zen\key\keywords.txt', 'w', encoding='utf-8') as f:
    for i in sorted_result:
        print(i)
        f.write(str(i)+'\n')



# fp = open(r'C:\roczhang\WHPU\zen\data\merged.txt','r',encoding='utf-8')
# content = fp.read()
#
# result = jieba.analyse.extract_tags(content, topK=20, withWeight=False,allowPOS=())
#
# result2 = jieba.analyse.textrank(content, topK=350, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
#
# with open(r'C:\roczhang\WHPU\zen\data\keywords.txt', 'w', encoding='utf-8') as f:
#     for i in result2:
#         f.write(i+'\n')