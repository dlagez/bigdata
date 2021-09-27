import os
import re
dir = '/Users/roczhang/Downloads/2016/'

# 1.读取文件夹里面的文件
files = os.listdir(dir)
strs = []
for file in files:
    with open(dir+file, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()  # 整行读取
            if not lines:  # 如果读到txt文件结尾了，读下一个文件
                break
            lines = lines.strip('\n')  # 去掉文件结尾的换行符号
            if len(lines) == 0:  # 如果读到空行，不记录
                continue
            strs.append(lines)
print(strs)


# 2.使用jieba分词器分词

import jieba

strs_seg = []
for str in strs:
    seg_list = jieba.cut(str, use_paddle=True)
    seg_list = list(seg_list)
    print(seg_list)
    strs_seg.append(seg_list)

print('********************* strs_seg *******************************')
print(strs_seg)      # 这里将所有的文本分词了，没有去重复，没有去标点

strs_seg = [i for item in strs_seg for i in item]     # 将所有文本放在一个列表里面

print('********************* set_strs *******************************')

set_strs = set(strs_seg)  # 去重
print(set_strs)

strs_list = list(set_strs)  # 转换成列表



# 这个函数是用来删除标点符号，数字和日期的。
def regex_change(line):
    #前缀的正则
    username_regex = re.compile(r"^\d+::")
    #URL，为了防止对中文的过滤，所以使用[a-zA-Z0-9]而不是\w
    url_regex = re.compile(r"""
        (https?://)?
        ([a-zA-Z0-9]+)
        (\.[a-zA-Z0-9]+)
        (\.[a-zA-Z0-9]+)*
        (/[a-zA-Z0-9]+)*
    """, re.VERBOSE|re.IGNORECASE)
    #剔除日期
    data_regex = re.compile(u"""        #utf-8编码
        年 |
        月 |
        日 |
        (周一) |
        (周二) | 
        (周三) | 
        (周四) | 
        (周五) | 
        (周六)
    """, re.VERBOSE)
    #剔除所有数字
    decimal_regex = re.compile(r"[^a-zA-Z]\d+")
    #剔除空格
    space_regex = re.compile(r"\s+")

    line = username_regex.sub(r"", line)
    line = url_regex.sub(r"", line)
    line = data_regex.sub(r"", line)
    line = decimal_regex.sub(r"", line)
    line = space_regex.sub(r"", line)

    return line

re_strs_list = regex_change(strs_list)