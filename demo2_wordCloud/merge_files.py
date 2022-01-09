import os
# 将一个文件夹的文件合并

path = r"C:\roczhang\WHPU\zen\2022 1 90"
file_list = os.listdir(path)
f = open(r'C:/roczhang/WHPU/zen/2022 1 90/merged.txt', 'w', encoding='utf-8')
for filename in file_list:
    filepath = path + '/' + filename
    for line in open(filepath, encoding='utf-8'):
        f.writelines(line)
f.close()


