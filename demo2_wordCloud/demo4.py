import matplotlib.pyplot as plt#绘图库
import jieba
from wordcloud import WordCloud
import imageio
# laptop上写的这个代码，由于win和mac不一样，所以它读文件需要使用utf-8
# 这个代码是第二份文件的，与demo3相比只是文件的位置不同。

stopwords = [line.strip() for line in
             open(r'C:\roczhang\WHPU\zen\词频图\停用词表.txt',
                  encoding='UTF-8').readlines()]
# 读入文本数据
fp = open(r'C:\roczhang\WHPU\zen\2022 1 9\merged.txt','r',encoding='utf-8')
content = fp.read()
# print(content)
#分词
words = jieba.lcut(content)
# 词频分析操作
data = {}
for word in words:
    if word not in stopwords and len(word) > 1:
        if word in data:
            data[word]+=1
        else:
            data[word]=1
# print(data)
"的" in stopwords
"的" in data.keys()



#排序
hist = list(data.items())#转成列表
hist.sort(key=lambda x:x[1],reverse=True)
# print(hist)

#调试输出
for i in range(20):
    # print(hist[i])
    print('{:<10}{:>5}'.format(hist[i][0],hist[i][1]))#左对齐10，右对齐5个长度

data.keys()

result = ' '.join(data)
img = imageio.imread(r"C:\roczhang\WHPU\zen\img\cycle.jpg")
# print(result)
#生成词云
wc = WordCloud(
    font_path=r'C:\roczhang\font\font.otf',
    background_color = 'white',#背景颜色
    width=500,#图片的宽
    height=300,
    max_font_size=30,
    min_font_size=5,
    mask=img,
)
wc.generate(result)

wc.to_file(r'C:\roczhang\WHPU\zen\img\2022 1 9.png')#保存图片
#显示图片
plt.figure('政府工作报告')
plt.imshow(wc)
plt.axis('off')#关闭坐标轴
plt.show()