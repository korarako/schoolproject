import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('norm.csv')
data_to_normalize = df['P'].values.reshape(-1, 1)
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data_to_normalize)
df['P'] = normalized_data
df.to_csv('norm.csv', index=False)
