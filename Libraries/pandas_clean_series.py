import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\full_practice_dataset.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())

print(df.isna().sum())
print(df.duplicated().sum())
df=df.drop_duplicates()
df=df.reset_index(drop=True)

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

df = df[((df["age"]>lower_bound)) & ((df["age"]<upper_bound))| (df["age"].isna())]

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
outliers = df[(df["marks"]<lower_bound) |  (df["marks"]>upper_bound)]
print(outliers)

df = df[((df["marks"]>=lower_bound)) & ((df["marks"]<=upper_bound)) | (df["marks"].isna())]

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
outliers = df[(df["attendance_pct"]<lower_bound) |  (df["attendance_pct"]>upper_bound)]
print(outliers)

df = df[((df["attendance_pct"]>=lower_bound)) & ((df["attendance_pct"]<=upper_bound)) | (df["attendance_pct"].isna())]

print(df["attendance_pct"])

print(df["attendance_pct"].isna().sum())
# fee column
df["fee_status"]=df["fee_status"].str.strip()
df["fee_status"] = df["fee_status"].replace(["N/A","-","","None","Unknown","Null","Na","Nan"],np.nan,regex=False)
print(df["fee_status"].isna().sum())

df["fee_status"] = df["fee_status"].fillna(df["fee_status"].mode()[0])
print(df["fee_status"].isna().sum())

# Date column 
df["join_date"] = pd.to_datetime(df["join_date"], format="mixed",errors="coerce")
print(df["join_date"].isna().sum())
df["join_date"]=df["join_date"].fillna(df["join_date"].mode()[0])
print(df["join_date"].isna().sum())
print(df["join_date"])
#printing the city
df["city"] = df["city"].str.strip().str.title()
df["city"] = df["city"].replace(["N/A","Null","-","None","Unknown","Na","Nan"],np.nan)


print(df["city"].isna().sum())

df["city"] = df["city"].fillna(df["city"].mode()[0])
print(df["city"].isna().sum())
print(df["city"])


# name columnn 
df["name"] = df["name"].str.strip().str.title()
print(df["name"])
print(df["name"].isna().sum())
# Guardain column 

df["guardian_name"] = df["guardian_name"].str.strip().str.title()
print(df["guardian_name"])
print(df["guardian_name"].isna().sum())



# phone number
df["phone"] = df["phone"].astype(str)
# remove symbols: + - ( ) and whitespace
df["phone"] = df["phone"].str.replace(r"[+\-\(\)\s]", "", regex=True)
# convert leading country code 92 back to a single 0
df["phone"] = df["phone"].str.replace(r"^92", "0", regex=True)
# sanity check the lengths
print("\nPhone number lengths:")
print(df["phone"].str.len().value_counts())
print(df["phone"])

print(df["fee_status"].isna().sum())


#checking the datset
print(df.head())

# save the dataset 

df.to_csv("Clean_Full_Practice_Dataset.csv",index=False)

#check 
df =pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\Clean_Full_Practice_Dataset.csv")
print(df.isna().sum())
print(df.duplicated().sum())