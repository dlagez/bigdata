### 实验一：主成分分析+数据可视化

数据：一个样本数据，一个标签。形状是：(112, 448)，(112, 1)，numpy格式。

要求：文件中的  T32data   是特征   需要进行一次  归一化   然后进行主成分分析  提取前三大主成分   进行可视化

结果：

<img src="README.assets/image-20210923135846213.png" alt="image-20210923135846213" style="zoom: 67%;" />

代码：[点我跳转](https://github.com/dlagez/bigdata/blob/master/demo1_analysis_plt/demo1_analysis_plt.py)    笔记：[点我跳转](https://github.com/dlagez/java-note-mac/blob/master/python/%E5%B0%8F%E5%AE%9E%E9%AA%8C/1.%E4%B8%BB%E6%88%90%E5%88%86%E5%88%86%E6%9E%90%26%E7%94%BB%E5%9B%BE.md)

<img src="README.assets/image-20210923161628631.png" alt="image-20210923161628631" style="zoom:67%;" />

代码：[点我跳转](https://github.com/dlagez/bigdata/blob/master/demo1_analysis_plt/demo2_analysis_plt.py)



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

