'''
@brief: 统计字数和词频
在laptop上跑的代码，给了我一个词汇表1.txt文件。这个文件里面的词作为目标词。
代码已修改，可以直接改文件名即可。关键词文件：合并。
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

def SplitWd(txt,wd_id,key_list):
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
    kw_sum = sum(dic.values()) # 总词数
    # 统计与环境相关词汇出现的频次
    # key_list = []
    # with open(r'C:\roczhang\WHPU\zen\合并350.txt', 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         if line != '\n':
    #             line = line.strip('\n')
    #             key_list.append(line)
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
                break
    key_sents = ''.join(key_sents)  # 核心字数

    # 核心字数（无符号）
    key_sents_u = unsign(key_sents)

    txt_u = unsign(txt)  # 总字数（无符号）

    with open(r'词汇词频分析_分立_city.csv', 'a', encoding='utf-8') as fp:
        fp.write("%s," % wd_id)
        for num in nums:
            fp.write("%s," % num)
        #                              ['总词数','核心字数（无符号）','总字数（无符号）','核心字数','总字数']
        fp.write('%s,%s,%s,%s,%s \n' % (kw_sum, len(key_sents_u),len(txt_u), len(key_sents),len(txt)))


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
    base = r'C:\roczhang\WHPU\zen\文档放这里'
    col_list = []
    col_list.append('文件名')
    key_list = []
    with open(r'C:\roczhang\WHPU\zen\分立350.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                line = line.strip('\n')
                key_list.append(line)

    with open(r'C:\roczhang\WHPU\zen\分立350.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                line = line.strip('\n')
                col_list.append(line)
    temp = ['总词数','核心字数（无符号）','总字数（无符号）','核心字数','总字数']
    col_list.extend(temp)
    # col_list =['文件名', '生态', '环境', '保护', '环境保护', '污染', '资源', '监测', '排放', '提高', '防治', '责任', '污染物',
    # '治理', '绿色', '强化', '监管', '规划', '督察', '环境监测', '预警', '保障', '红线', '监督', '农业', '环境保护部', '流域',
    # '水资源', '整治', '公园', '优化', '改善', '农村', '排污', '应急', '损害', '土壤环境', '大气', '水源', '能源', '环境质量',
    # '改造', '节能', '土地', '耕地', '地下水', '管控', '违法', '维护', '水质', '示范', '用水', '煤炭', '海洋', '饮用水', '草原',
    # '淘汰', '燃煤', '回收', '土壤', '责令', '节水', '污染源', '产能', '环境治理', '农产品', '水体', '河湖', '垃圾', '检查',
    # '减排', '破坏', '环境污染', '养殖', '海域', '严格控制', '覆盖', '森林', '节约', '整改', '防控', '达标', '违反', '污水',
    # '基础设施', '损害赔偿', '监督管理', '环境影响', '重金属', '畜禽', '生态环境', '绿色发展', '自然资源', '土地资源', '农业面污染防治',
    # '自然资源资产离任审计', '自然资源资产负债表', '中央环境保护督察','总词数','核心字数（无符号）','总字数（无符号）','核心字数','总字数']
    #
    with open(r'词汇词频分析_分立_city.csv', 'a', encoding='utf-8') as fp:
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
        SplitWd(content,wd_id, key_list)
        # print(Path)


if __name__ == '__main__':
    main()
    print('执行完成！')

    # col_list =['文件名','环境保护','环保','污染','生态','生态环境','生态文明','污染','减排','排污','能耗','水耗','污水处理','污水治理','污染防治','节水','水土保持','再利用','节能','节约','可持续发展','新能源','低碳','绿色','绿化','绿色发展','空气','饮水安全','水质','化学需氧量','氨氮','二氧化硫','二氧化碳','PM10','PM2.5','自然资源','土地资源','耕地','水资源','矿山','森林','海洋','草原','土壤','蓝天','碧水','净土','农业面污染防治','自然资源资产离任审计','自然资源资产负债表','河长制','湖长制','中央环境保护督察','总词数','核心字数（无符号）','总字数（无符号）','核心字数','总字数']
    # print(len(col_list))

# words = []
# with open('C:/roczhang/tmp/词汇表1.txt', 'r', encoding='utf-8') as file:
#     words = [line.strip('\n') for line in file.readlines()]
