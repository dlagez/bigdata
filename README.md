### 实验一：主成分分析+数据可视化

数据：一个样本数据，一个标签。形状是：(112, 448)，(112, 1)，numpy格式。

要求：文件中的  T32data   是特征   需要进行一次  归一化   然后进行主成分分析  提取前三大主成分   进行可视化

结果：

<img src="https://cdn.jsdelivr.net/gh/dlagez/img@master/image-20220104192718040.png" alt="image-20220104192718040" style="zoom: 50%;" />

代码：[点我跳转](https://github.com/dlagez/bigdata/blob/master/demo1_analysis_plt/demo1_analysis_plt.py)    笔记：[点我跳转](https://github.com/dlagez/java-note-mac/blob/master/python/%E5%B0%8F%E5%AE%9E%E9%AA%8C/1.%E4%B8%BB%E6%88%90%E5%88%86%E5%88%86%E6%9E%90%26%E7%94%BB%E5%9B%BE.md)

<img src="https://cdn.jsdelivr.net/gh/dlagez/img@master/image-20220104192806415.png" alt="image-20220104192806415" style="zoom:50%;" />

代码：[点我跳转](https://github.com/dlagez/bigdata/blob/master/demo1_analysis_plt/demo2_analysis_plt.py)

### 实验二：LSA（潜在语意分析）

数据：有八个文本文件：

<img src="https://cdn.jsdelivr.net/gh/dlagez/img@master/image-20220104192824619.png" alt="image-20220104192824619" style="zoom: 33%;" />

里面的内容是这个样子的：

```
（五）自然资源资产审计情况

对咸阳市、太白等“一市四县”领导干部自然资源资产责任情况开展试审。发现的主要问题：30个工业园区均未进行水资源规划论证，也未编制水土保持方案；矿山环境治理缓慢，生态恢复不到位；建设用地超规划；8个县（区）违规采砂、采石，占用河道、农田、耕地等；4个市县地下水超采严重，取水许可管理不到位；4个市县欠收水资源费、水土保持费等；3个市县挤占挪用截留专项资金；部分市县未实现城市雨污分流。

对宝鸡、渭南等7个市及所属县区2011年至2015年水污染防治资金管理及使用情况开展了审计，发现的主要问题：25个市县相关部门滞留挤占挪用专项资金；11个县区专项资金闲置超过6个月；16个县区财政配套资金未落实；17个项目建设未及时开工；56个项目建设未及时完工；14个项目违规招投标；36个项目基本建设程序不完整。
```

1.首先需要将里面的标点，数字去除。保留文本信息。

2.使用jieba分词器将词的文本提取出来。类似于下面的这个样子，只需要汉字。

```
七环境保护审计情况一自然资源资产离任审计情况按照省政府部署省审计厅组织实施了黔西南州本级及个县区领导干部自然资源资产离任审计从审计情况看这些地区大力推进生态文明建设生态环境质量逐步改善自然资源管理和环境保护总体较好审计发现的问题主要有一是森林资源管理方面存在违法征占用林地擅
```

```python
# 只保留中文，去除所有的标点以及数字。
lines = re.sub('[^\u4e00-\u9fa5]+', '', lines)
```



### 实验三：生成词云图

数据：

<img src="https://cdn.jsdelivr.net/gh/dlagez/img@master/image-20220104191310663.png" alt="image-20220104191310663" style="zoom: 33%;" />

一个文件夹的数据，需要将这些`txt`文件合并到一个文件[代码](https://github.com/dlagez/bigdata/blob/master/demo2_wordCloud/merge_files.py)：

文件长这个样子：

<img src="https://cdn.jsdelivr.net/gh/dlagez/img@master/image-20220104192007110.png" alt="image-20220104192007110" style="zoom: 33%;" />

使用jieba分词[代码](https://github.com/dlagez/bigdata/blob/master/demo2_wordCloud/demo.py)，然后使用这些词生成词云图即可。



txt处理：

merge a

将一个文件夹的txt文本合并到一个文本里面。code

```python
import os
path = "/Volumes/roczhang/WHPU/zen/text2"
file_list = os.listdir(path)
f = open('/Volumes/roczhang/WHPU/zen/merged.txt', 'w')
for filename in file_list:
    filepath = path + '/' + filename
    for line in open(filepath):
        f.writelines(line)
f.close()
```



把列表以txt形式的保存与读取.[code](https://github.com/dlagez/bigdata/blob/master/demo3_/test.py)

```python
key_list = ['环境保护', '环保', '污染', '生态', '生态环境', '生态文明', '污染', '减排', '排污', '能耗', '水耗', '污水处理', '污水治理', '污染防治', '节水',
            '水土保持', '再利用', '节能', '节约', '可持续发展', '新能源', '低碳', '绿色', '绿化', '绿色发展', '空气', '饮水安全', '水质', '化学需氧量', '氨氮',
            '二氧化硫', '二氧化碳', 'PM10', 'PM2.5', '自然资源', '土地资源', '耕地', '水资源', '矿山', '森林', '海洋', '草原', '土壤', '蓝天', '碧水',
            '净土', '农业面污染防治', '自然资源资产离任审计', '自然资源资产负债表', '河长制', '湖长制', '中央环境保护督察']

with open('/Volumes/roczhang/temp/list.txt', 'w') as f:
    for i in key_list:
        f.write(i+'\n')

file = open('/Volumes/roczhang/temp/list.txt')
lines = file.readlines()
for line in lines:
    line = line.strip('\n')
    print(line)

read_line = []
for line in lines:
    line = line.strip('\n')
    read_line.append(line)
```



word to txt

把一个文件夹的word文档转换成相应的txt文件。只会读取文字。[code](https://github.com/dlagez/bigdata/blob/master/demo3_/word_to_txt.py)

```python
from docx import Document
import os
# 将一个文件夹的word文件转换称txt文件
path = '/Volumes/roczhang/WHPU/zen/政策文本'
path_txt = '/Volumes/roczhang/WHPU/zen/test'  # 这个文件夹用来装txt文件
file_list = os.listdir(path)  # 读取出docx文件夹所有的文件名字

for file in file_list:
    file_path = path + '/' + file
    # print(file_path)
    doc = Document(file_path)  # 读取docx文件
    f = open(path_txt + '/' + file.split('.')[0] + '.txt', 'a')  # 把.docx的后缀改成txt，并创建txt文件。
    print(file_path + '\n')
    for paragraph in doc.paragraphs:
        f.write(paragraph.text)  # 将docx段落写入txt文件
        print(paragraph.text + '\n')
    f.close()  # txt文件使用完成后关闭

# 更好的写法
for file in file_list:
    file_path = path + '/' + file
    # print(file_path)
    doc = Document(file_path)  # 读取docx文件
    with open(path_txt + '/' + file.split('.')[0] + '.txt', 'a') as f:
        for paragraph in doc.paragraphs:
            f.write(paragraph.text)  # 将docx段落写入txt文件
            print(paragraph.text + '\n')
```



将二维list写入文件

```python
output = open('/Volumes/roczhang/WHPU/zen/result.txt', 'w')
for i in range(len(result)):
    output.write('第' + str(i) + '篇文章!' + '\n')  # 在每篇（每一行开始的时候做一个标记）
    for j in range(len(result[i])):
        # print(result[i][j])
        output.write(str(result[i][j]))  # 写入一行数据
        output.write(' ')
    output.write('\n\n')  # 每写完一行数据之后按两次回撤键
output.close()
```

效果是这样的

![image-20220107162556713](https://cdn.jsdelivr.net/gh/dlagez/img@master/image-20220107162556713.png)

conda环境：使用的是mac m1 Miniforge

```bash
// 环境信息
matplotlib                3.4.3
numpy                     1.21.2
pandas                    1.3.3           
python                    3.8.12          
scikit-learn              0.24.2           
scipy                     1.7.0            
seaborn                   0.11.2            
```





