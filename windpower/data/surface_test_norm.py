import pandas as pd

# 读取 CSV 文件，指定没有表头
df = pd.read_csv('surface_test.csv', header=None)

# 对第一列数据进行标准化处理
col1 = df[0]
col1_norm = (col1 - col1.mean()) / col1.std()

# 将处理后的数据保存到新的 CSV 文件中，手动添加表头
df_norm = pd.DataFrame({'Column1_norm': col1_norm, 'Column2': df[1]})
df_norm.to_csv('surface_test_norm.csv', index=False, header=['Column1_norm', 'Column2'])

