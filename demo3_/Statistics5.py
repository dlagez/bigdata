'''
@brief: 统计字数和词频
在laptop上跑的代码，给了我一个词汇表1.txt文件。这个文件里面的词作为目标词。
代码已修改，可以直接改文件名即可。关键词文件：分立
'''
import os
import re
import jieba
from docx import Document

def makeid(Path):
    rmv = ['文档放这里', '/', '.docx']
    for rmk in rmv:
        Path = Path.replace(rmk, '')
    return Path

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

def findocx(base):
    for Path in findAllFile(base):
        if 'docx' in Path:
            yield Path

def unsign(txt):
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~“”？，！【】（）、。：；’‘……￥·"""
    dicts={i:'' for i in punctuation}
    punc_table=str.maketrans(dicts)
    untxt=txt.translate(punc_table)
    return untxt

def cut_sent(para):
    para = re.sub('([。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split("\n")

def SplitWd(txt,wd_id):
    words = jieba.lcut(txt)
    # 词频分析操作
    dic = {}
    for word in words:
        if len(word)>1:
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=1
    #报告全文词频总数
    kw_num = len(dic)#关键词个数
    kw_sum = sum(dic.values())#词频总数
    # 统计与环境相关词汇出现的频次
    key_list = []
    with open(r'C:\roczhang\WHPU\zen\分立350.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                line = line.strip('\n')
                key_list.append(line)
    # key_list = ['生态', '保护', '环境', '环境保护', '生态环境', '污染', '排放', '防治', '资源', '自然资源', '监测', '水', '治理', '污染物', '绿色', '环保', '环境保护部', '督察', '红线', '大气污染', '水资源', '损害', '整治', '大气', '土壤污染', '排污', '预警', '自然', '健康', '土壤环境', '环境质量', '节能', '环境监测', '水源', '耕地', '土地', '生态系统', '地下水', '清洁']
    nums = []
    for kw in key_list:
        try:
            num = dic[kw]
        except:
            num = 0
        nums.append(num)

    # 统计含关键词句子的词数
    sents = cut_sent(txt)
    key_sents = [] 
    for sent in sents:
        for key in key_list:
            if key in sent:
                key_sents.append(sent)
    key_sents = ''.join(key_sents)

    key_sents_u = unsign(key_sents)
    txt_u = unsign(txt)

    with open(r'词汇词频分析_分立.csv','a', encoding='utf-8') as fp:
        fp.write("%s," % wd_id)
        for num in nums:
            fp.write("%s," % num)
        fp.write('%s,%s,%s,%s,%s \n' % (kw_sum, len(key_sents_u),len(txt_u), len(key_sents),len(txt)))
        # fp.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'
        #          '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n'
        #          % (wd_id, nums[0], nums[1], nums[2], nums[3],nums[4], nums[5], nums[6], nums[7],nums[8], nums[9],
        #             nums[10], nums[11],nums[12], nums[13], nums[14], nums[15],nums[16], nums[17], nums[18], nums[19],
        #             nums[20], nums[21], nums[22], nums[23],nums[24],nums[25], nums[26], nums[27], nums[28],nums[29],
        #             nums[30], nums[31], nums[32],nums[33], nums[34], nums[35], nums[36],nums[37], nums[38], kw_sum,
        #             len(key_sents_u),len(txt_u), len(key_sents),len(txt)))
        #

def Readfl(Path):
    try:
        docs = Document(Path)
    except:
        return 0, makeid(Path)
    doc = []
    all_para = docs.paragraphs
    for para in all_para:
        # print(para.text)
        doc.append(para.text)
    text = ''.join(doc)
    # print(text)

    return text, makeid(Path)

def main():
    base = r'C:\roczhang\WHPU\zen\政策文本'
    col_list = []
    col_list.append('文件名')
    with open(r'C:\roczhang\WHPU\zen\合并350.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                line = line.strip('\n')
                col_list.append(line)
    temp = ['总词数','核心字数（无符号）','总字数（无符号）','核心字数','总字数']
    col_list.extend(temp)
    # col_list =['文件名','生态', '保护', '环境', '环境保护', '生态环境', '污染', '排放', '防治', '资源', '自然资源', '监测', '水',
    #            '治理', '污染物', '绿色', '环保', '环境保护部', '督察', '红线', '大气污染', '水资源', '损害', '整治', '大气',
    #            '土壤污染', '排污', '预警', '自然', '健康', '土壤环境', '环境质量', '节能', '环境监测', '水源', '耕地', '土地',
    #            '生态系统', '地下水', '清洁','总词数','核心字数（无符号）','总字数（无符号）','核心字数','总字数']
    #
    with open(r'词汇词频分析_分立.csv','a', encoding='utf-8') as fp:
        for line in col_list[:-1]:
            fp.write("%s," % line)
        fp.write("%s \n" % col_list[-1])
        # fp.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'
        #          '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n' % tuple(col_list))

    for Path in findocx(base):
        # flist = os.path.split(i)
        content,wd_id = Readfl(Path)
        if content == 0:
            content = ''
        SplitWd(content,wd_id) 
        # print(Path)


if __name__ == '__main__':
    main()
    print('执行完成！')

    # col_list =['文件名','环境保护','环保','污染','生态','生态环境','生态文明','污染','减排','排污','能耗','水耗','污水处理','污水治理','污染防治','节水','水土保持','再利用','节能','节约','可持续发展','新能源','低碳','绿色','绿化','绿色发展','空气','饮水安全','水质','化学需氧量','氨氮','二氧化硫','二氧化碳','PM10','PM2.5','自然资源','土地资源','耕地','水资源','矿山','森林','海洋','草原','土壤','蓝天','碧水','净土','农业面污染防治','自然资源资产离任审计','自然资源资产负债表','河长制','湖长制','中央环境保护督察','总词数','核心字数（无符号）','总字数（无符号）','核心字数','总字数']
    # print(len(col_list))

# words = []
# with open('C:/roczhang/tmp/词汇表1.txt', 'r', encoding='utf-8') as file:
#     words = [line.strip('\n') for line in file.readlines()]
