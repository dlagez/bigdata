import numpy as np
import scipy.io as scio
from sklearn import preprocessing
import sklearn.decomposition as dp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1.读取数据
X_norm = scio.loadmat("/Volumes/roczhang/download/data/2071/T32data.mat")['DATA']
y = scio.loadmat("/Volumes/roczhang/download/data/2071/T32label.mat")['label']


print(X_norm.shape)
print(y.shape)

# 2.归一化 将每一列的特征归一化
# X_norm = preprocessing.normalize(X, norm='l2', axis=0)  # axis=0 竖着规范每个特征

# 3.主成分分析，选取三个主成分
pca = dp.PCA(n_components=3)
pca.fit(X_norm)
# print(pca.explained_variance_ratio_)
X_new = pca.transform(X_norm)

# 4.合并两个数组 使用不同的颜色和形状来显示不同类型的数据。
Xy = np.concatenate((X_new, y), axis=1)
print(len(Xy))
print(Xy[4][3])

# 5.定义两个数组，分别用来存储0，1类别的数据
zero = []
one = []
other = []
print(range(len(Xy)))

# 6.将数据分装
for i in range(len(Xy)):
    if (Xy[i][3] == 0):
        zero.append(Xy[i])
    elif(Xy[i][3] == 1):
        one.append(Xy[i])
    else:
        print("第i行的标签不是0或1：", i)

# 7.将分装的数据转换成numpy格式
one_norm = np.array(one)
print(one_norm.shape)

zero_norm = np.array(zero)
print(zero_norm.shape)

# 8.画图
azim = -20
elev = 15

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 将类别为1的数据画到figure上面
ax.scatter(one_norm[:, 0], one_norm[:, 1], one_norm[:, 2], c='r', marker='o')
# 将类别为0的数据画到figure上面
ax.scatter(zero_norm[:, 0], zero_norm[:, 1], zero_norm[:, 2], c='b', marker='^')
ax.view_init(elev, azim)
# 9.设置xyz轴
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
# 10.显示图像
plt.show()

# print('ax.azim {}'.format(ax.azim))
# print('ax.elev {}'.format(ax.elev))


