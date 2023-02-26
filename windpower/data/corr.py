import pandas as pd
import matplotlib.pyplot as plt
# 读取 CSV 文件
df = pd.read_csv('123123.csv')

x = df['Column1_norm']
y = df['Column2']
# 计算两列数据的相关系数
corr = x.corr(y)

# 打印相关系数
print('相关系数为：', corr)
