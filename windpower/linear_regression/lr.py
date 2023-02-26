import pandas as pd
from sklearn.linear_model import LinearRegression

# 读取CSV文件
df = pd.read_csv('data.csv', header=0)

# 提取X和y
X = df.iloc[:, :6].values
y = df.iloc[:, 6].values

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X, y)

# 输出模型参数
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
