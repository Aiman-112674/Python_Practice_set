import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\full_practice_dataset.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())

print(df.isna().sum())
print(df.duplicated().sum())

print(df["email"].duplicated().sum())
print(df["phone"].duplicated().sum())
# print(df["name"].duplicated().sum())

# age column 

print(df["age"])
Q1 = df["age"].quantile(0.25)
Q3 = df["age"].quantile(0.75)


IQR = Q3-Q1
print("Q1:" , Q1)
print("Q3:" , Q3)
print("IQR:" , IQR)
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR
print("Lower_bound:", lower_bound)
print("upper_bound:", upper_bound)
outliers = df[(df["age"]<=lower_bound) |  (df["age"]>=upper_bound)]
print(outliers)

df = df[(df["age"]>=lower_bound) & (df["age"]<=upper_bound)]

print(df)

# marks
df["marks"] = df["marks"].str.replace("kg", "",regex=False)
df["marks"] = df["marks"].str.replace("pts","",regex=False)
df["marks"] = df["marks"].str.replace("marks","",regex=False)
df["marks"] = df["marks"].str.replace("-","",regex=False)
df["marks"] = pd.to_numeric(df["marks"],errors = "coerce")
print(df["marks"])

Q1 = df["marks"].quantile(0.25)
Q3 = df["marks"].quantile(0.75)


IQR = Q3-Q1
print("Q1:" , Q1)
print("Q3:" , Q3)
print("IQR:" , IQR)
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR
print("Lower_bound:", lower_bound)
print("upper_bound:", upper_bound)
outliers = df[(df["marks"]<=lower_bound) |  (df["marks"]>=upper_bound)]
print(outliers)

df = df[(df["marks"]>=lower_bound) & (df["marks"]<=upper_bound)]

print(df["marks"].isna().sum())
df["marks"] = df["marks"].fillna(df["marks"].mean())
print(df["marks"].isna().sum())

# attendence 

print(df["attendance_pct"].isna().sum())
print(df["attendance_pct"].dtypes)

df["attendance_pct"]=pd.to_numeric(df["attendance_pct"],errors="coerce")
print(df["attendance_pct"].dtypes)

Q1 = df["attendance_pct"].quantile(0.25)
Q3 = df["attendance_pct"].quantile(0.75)


IQR = Q3-Q1
print("Q1:" , Q1)
print("Q3:" , Q3)
print("IQR:" , IQR)
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR
print("Lower_bound:", lower_bound)
print("upper_bound:", upper_bound)
outliers = df[(df["attendance_pct"]<=lower_bound) |  (df["attendance_pct"]>=upper_bound)]
print(outliers)

df = df[(df["attendance_pct"]>=lower_bound) & (df["attendance_pct"]<=upper_bound)]

print(df["attendance_pct"])

print(df["attendance_pct"].isna().sum())

df["fee_status"] = df["fee_status"].str.replace("-","",regex=False)
print(df["fee_status"].isna().sum())

df["fee_status"] = df["fee_status"].fillna(df["fee_status"].mode()[0])
print(df["fee_status"].isna().sum())

# phone number 

print(df["phone"].isna().sum())
print(df["phone"].duplicated().sum())
print(df(df["phone"]).duplicated())