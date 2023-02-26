import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as op
from scipy.optimize import curve_fit

# 需要拟合的函数
def f_1(x, A, B, C):
    return A * x**2 + B * x + C

# 打开CSV文件并读取前480行的第3列和第4列
with open('real.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    col3_data = []
    col4_data = []
    for i, row in enumerate(csv_reader):
        if i == 0:
            continue  # 跳过CSV文件的标题行
        if i > 480:
            break  # 读取前480行
        col3_data.append(float(row[2]))
        col4_data.append(float(row[3]))

# 将数据转换为NumPy数组格式
x_data = np.array(col4_data)
y_data = np.array(col3_data)

# 需要拟合的数据组
x_group = x_data
y_group = y_data
# 得到返回的A，B值
A, B, C = op.curve_fit(f_1, x_group, y_group)[0]

# 数据点与原先的进行画图比较
plt.scatter(x_group, y_group, marker='o',label='His_Power')
x = np.arange(0, 15, 0.01)
y = A * x**2 + B *x + C
plt.plot(x, y,color='red',label='fitting_curve')
plt.legend() # 显示label

plt.show()
print(A, B, C)