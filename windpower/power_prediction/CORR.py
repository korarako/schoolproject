import pandas as pd

# 读取CSV文件
df = pd.read_csv('output.csv', header=0)

# 从第11列和第12列获取数据
data1 = df.iloc[:, 10].values
data2 = df.iloc[:, 11].values

# 计算相关系数
corr = pd.Series(data1).corr(pd.Series(data2))

# 输出相关系数
print("Correlation Coefficient:", corr)
