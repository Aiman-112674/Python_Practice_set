
import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\student_dataset_v2.csv")
print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
print(df[df["Age"]>20])