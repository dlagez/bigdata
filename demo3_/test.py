key_list = ['环境保护', '环保', '污染', '生态', '生态环境', '生态文明', '污染', '减排', '排污', '能耗', '水耗', '污水处理', '污水治理', '污染防治', '节水',
            '水土保持', '再利用', '节能', '节约', '可持续发展', '新能源', '低碳', '绿色', '绿化', '绿色发展', '空气', '饮水安全', '水质', '化学需氧量', '氨氮',
            '二氧化硫', '二氧化碳', 'PM10', 'PM2.5', '自然资源', '土地资源', '耕地', '水资源', '矿山', '森林', '海洋', '草原', '土壤', '蓝天', '碧水',
            '净土', '农业面污染防治', '自然资源资产离任审计', '自然资源资产负债表', '河长制', '湖长制', '中央环境保护督察']

with open('/Volumes/roczhang/temp/list.txt', 'w') as f:
    for i in key_list:
        f.write(i+'\n')


file = open(r'C:\roczhang\WHPU\zen\合并350.txt', 'r', encoding='utf-8')
lines = file.readlines()
for line in lines:
    line = line.strip('\n')
    print(line)

read_line = []
for line in lines:
    line = line.strip('\n')
    read_line.append(line)

