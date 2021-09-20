import pandas as pd
import tensorflow as tf

file1 = 'D:/금융/UPRO_historical_data.csv'
bb = pd.read_csv(file1)
print(bb.columns)
bb.head()