import pandas as pd
import numpy as np
df = pd.read_csv("dataset/data.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())