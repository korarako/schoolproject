import pandas as pd
from sklearn.metrics import mean_squared_error

# 读取CSV文件
df = pd.read_csv('output.csv', header=0)

# 从第11列和第12列获取数据
y_true = df.iloc[:, 10].values
y_pred = df.iloc[:, 11].values

# 计算MSE
mse = mean_squared_error(y_true, y_pred)

# 输出MSE
print("MSE:", mse)
