import pandas as pd

# 定义一个自定义函数f
def f(x):
    return 0.01820559371764693 * x ** 2 - 0.08908227831338669 * x + 0.10894957907797545

# 读取CSV文件
df = pd.read_csv('output.csv', header=0)

# 从第10列获取数据
data = df.iloc[:, 9].values

# 对数据应用f函数
result = [f(x) for x in data]

# 将结果添加到DataFrame中
df['Pred Power'] = result

# 将DataFrame写入CSV文件
df.to_csv('output.csv', index=False)
