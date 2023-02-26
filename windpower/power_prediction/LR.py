import pandas as pd
from sklearn.linear_model import LinearRegression

# 读取CSV文件
df = pd.read_csv('result.csv', header=0)

# 提取X和y
X = df.iloc[:, :6].values
y = df.iloc[:, 6].values

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X, y)

# 进行预测
y_pred = model.predict(X)

# 将预测结果添加到DataFrame中
df['Prediction'] = y_pred

# 将DataFrame写入CSV文件
df.to_csv('output.csv', index=False)
