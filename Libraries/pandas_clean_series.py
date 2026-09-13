# import pandas as pd
# import numpy as np


# df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\full_practice_dataset.csv")
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())

# print(df.isna().sum())
# print(df.duplicated().sum())
# df=df.drop_duplicates()
# df=df.reset_index(drop=True)

# print(df["email"].duplicated().sum())
# print(df["phone"].duplicated().sum())
# # print(df["name"].duplicated().sum())

# # age column 

# print(df["age"])
# Q1 = df["age"].quantile(0.25)
# Q3 = df["age"].quantile(0.75)


# IQR = Q3-Q1
# print("Q1:" , Q1)
# print("Q3:" , Q3)
# print("IQR:" , IQR)
# lower_bound = Q1-1.5*IQR
# upper_bound = Q3+1.5*IQR
# print("Lower_bound:", lower_bound)
# print("upper_bound:", upper_bound)
# outliers = df[(df["age"]<=lower_bound) |  (df["age"]>=upper_bound)]
# print(outliers)

# df = df[((df["age"]>lower_bound)) & ((df["age"]<upper_bound))| (df["age"].isna())]

# print(df)

# # marks
# df["marks"] = df["marks"].str.replace("kg", "",regex=False)
# df["marks"] = df["marks"].str.replace("pts","",regex=False)
# df["marks"] = df["marks"].str.replace("marks","",regex=False)
# df["marks"] = df["marks"].str.replace("-","",regex=False)
# df["marks"] = pd.to_numeric(df["marks"],errors = "coerce")
# print(df["marks"])

# Q1 = df["marks"].quantile(0.25)
# Q3 = df["marks"].quantile(0.75)


# IQR = Q3-Q1
# print("Q1:" , Q1)
# print("Q3:" , Q3)
# print("IQR:" , IQR)
# lower_bound = Q1-1.5*IQR
# upper_bound = Q3+1.5*IQR
# print("Lower_bound:", lower_bound)
# print("upper_bound:", upper_bound)
# outliers = df[(df["marks"]<lower_bound) |  (df["marks"]>upper_bound)]
# print(outliers)

# df = df[((df["marks"]>=lower_bound)) & ((df["marks"]<=upper_bound)) | (df["marks"].isna())]

# print(df["marks"].isna().sum())
# df["marks"] = df["marks"].fillna(df["marks"].mean())
# print(df["marks"].isna().sum())

# # attendence 

# print(df["attendance_pct"].isna().sum())
# print(df["attendance_pct"].dtypes)

# df["attendance_pct"]=pd.to_numeric(df["attendance_pct"],errors="coerce")
# print(df["attendance_pct"].dtypes)

# Q1 = df["attendance_pct"].quantile(0.25)
# Q3 = df["attendance_pct"].quantile(0.75)


# IQR = Q3-Q1
# print("Q1:" , Q1)
# print("Q3:" , Q3)
# print("IQR:" , IQR)
# lower_bound = Q1-1.5*IQR
# upper_bound = Q3+1.5*IQR
# print("Lower_bound:", lower_bound)
# print("upper_bound:", upper_bound)
# outliers = df[(df["attendance_pct"]<lower_bound) |  (df["attendance_pct"]>upper_bound)]
# print(outliers)

# df = df[((df["attendance_pct"]>=lower_bound)) & ((df["attendance_pct"]<=upper_bound)) | (df["attendance_pct"].isna())]

# print(df["attendance_pct"])

# print(df["attendance_pct"].isna().sum())
# # fee column
# df["fee_status"]=df["fee_status"].str.strip()
# df["fee_status"] = df["fee_status"].replace(["N/A","-","","None","Unknown","Null","Na","Nan"],np.nan,regex=False)
# print(df["fee_status"].isna().sum())

# df["fee_status"] = df["fee_status"].fillna(df["fee_status"].mode()[0])
# print(df["fee_status"].isna().sum())

# # Date column 
# df["join_date"] = pd.to_datetime(df["join_date"], format="mixed",errors="coerce")
# print(df["join_date"].isna().sum())
# df["join_date"]=df["join_date"].fillna(df["join_date"].mode()[0])
# print(df["join_date"].isna().sum())
# print(df["join_date"])
# #printing the city
# df["city"] = df["city"].str.strip().str.title()
# df["city"] = df["city"].replace(["N/A","Null","-","None","Unknown","Na","Nan"],np.nan)


# print(df["city"].isna().sum())

# df["city"] = df["city"].fillna(df["city"].mode()[0])
# print(df["city"].isna().sum())
# print(df["city"])


# # name columnn 
# df["name"] = df["name"].str.strip().str.title()
# print(df["name"])
# print(df["name"].isna().sum())
# # Guardain column 

# df["guardian_name"] = df["guardian_name"].str.strip().str.title()
# print(df["guardian_name"])
# print(df["guardian_name"].isna().sum())



# # phone number
# df["phone"] = df["phone"].astype(str)
# # remove symbols: + - ( ) and whitespace
# df["phone"] = df["phone"].str.replace(r"[+\-\(\)\s]", "", regex=True)
# # convert leading country code 92 back to a single 0
# df["phone"] = df["phone"].str.replace(r"^92", "0", regex=True)
# # sanity check the lengths
# print("\nPhone number lengths:")
# print(df["phone"].str.len().value_counts())
# print(df["phone"])

# print(df["fee_status"].isna().sum())


# #checking the datset
# print(df.head())

# # save the dataset 

# df.to_csv("Clean_Full_Practice_Dataset.csv",index=False)

# #check 
# df =pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\Clean_Full_Practice_Dataset.csv")
# print(df.isna().sum())
# print(df.duplicated().sum())

# KNN Imputer

import pandas as pd
import numpy as np 
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\full_practice_dataset.csv")

print(df["student_id"].isna().sum())
print(df.head())
print(df.shape)
print(df.isna().sum())
print(df.duplicated().sum())

# wrong formatted values 
#marks
df["marks"] = df["marks"].astype(str).str.replace("marks","",regex=False)
df["marks"] = df["marks"].str.replace("pts","",regex=False)
df["marks"] = df["marks"].str.replace("kg","",regex=False)
df["marks"] = df["marks"].replace(["NA","none","-"],np.nan)
df["marks"] = pd.to_numeric(df["marks"],errors="coerce")
print(df["marks"].head(12))
#attendance 
df["attendance_pct"] = df["attendance_pct"].astype(str).str.replace("%","",regex=False)
df["attendance_pct"] = pd.to_numeric(df["attendance_pct"],errors="coerce")
#age 
df["age"] = pd.to_numeric(df["age"],errors="coerce")
#fee_status 
df["fee_status"] = df["fee_status"].str.strip().str.title()
df["fee_status"] = df["fee_status"].replace(["N/A","Null","-","","None","Unknown","Na","Nan"], np.nan)
df["fee_status"] = df["fee_status"].fillna(df["fee_status"].mode()[0])
print(df["fee_status"].isna().sum())
# datetime
print(df["join_date"].isna().sum())          # before fillna - how many nulls?
print(df["join_date"].mode())                  # what does mode() actually return?
print(df["join_date"].mode()[0])                # what's the single value being used to fill?
df["join_date"] = df["join_date"].fillna(df["join_date"].mode()[0])
print(df["join_date"].isna().sum())     
# city 
df["city"] = df["city"].str.strip().str.title()
df["city"] = df["city"].replace(["N/A","Null","-","","None","Unknown","Na","Nan"], np.nan)
df["city"] = df["city"].fillna(df["city"].mode()[0])

print(df["city"].isna().sum())     # should now genuinely be 0
print(df["city"].unique())      

print(df.isna().sum())

#checking the null values in these three numeric columns 
print(df[["age","marks","attendance_pct"]].isna().sum())

numeric_columns =["age","marks","attendance_pct"]
numeric_df = df[numeric_columns]

print("Null Values Before KNN: ")
print(numeric_df.isna().sum())

#scale first 
scaler = StandardScaler()
scaled = scaler.fit_transform(numeric_df)
print(scaled)
#impute
imputer = KNNImputer(n_neighbors=3)
imputed_scaled = imputer.fit_transform(scaled)

# convert back to original scale 
imputed_original = scaler.inverse_transform(imputed_scaled)
imputed_df= pd.DataFrame(imputed_original,columns=numeric_columns,index=df.index)

df["age"] = imputed_df["age"]
df["marks"] = imputed_df["marks"]
df["attendance_pct"] = imputed_df["attendance_pct"]
print("Null Values After KNN")
print(df[["age","attendance_pct","marks"]].isna().sum())

print(df[["age","attendance_pct","marks"]].describe())


print(df.duplicated().sum())

# checking duplication in each column
for col in df.columns:
    count = df[col].duplicated().sum()
    print(f"{col} : {count} duplicated values")

# checking the student id and email and phone number got [8,8,6] duplicated values lets slow them 
dup_ids = df[df["student_id"].duplicated(keep=False)]
print(dup_ids.sort_values("student_id"))


#checking the 
print(df[df["student_id"].isna()])
print(df[df["student_id"].isna()].index)
print(df.index.duplicated().sum())    # check if your index has repeated labels (a common cause!)
print(df.dtypes)

print("Before removing duplicates:", df["student_id"].duplicated().sum())   # should show 8

df = df.drop_duplicates()
df = df.reset_index(drop=True)
print("After removing duplicates:", df["student_id"].duplicated().sum())   # should now show 0

dup_ids = df[df["student_id"].duplicated(keep=False)]
print(dup_ids.sort_values("student_id"))
df = df.drop_duplicates(subset="student_id", keep="first")
print(df["student_id"].duplicated().sum())

# Quick check 
print(df.shape)
print(df["student_id"].isna().sum())
print(df["student_id"].duplicated().sum())
print(df["student_id"].dtype)   

print(df["email"].duplicated().sum())

#Outliers 

print(df[["age","marks","attendance_pct"]].describe())
#Age
# find the IQR
Q1 = df["age"].quantile(0.25)
Q3 = df["age"].quantile(0.75)
IQR = Q3-Q1
print("Q1:",Q1)
print("Q3:",Q3)
print("IQR:",IQR)

# finding conditions for outlier 
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR

print("Lower_Bound:",lower_bound)
print("upper_Bound:",upper_bound)

# detecting outliers 

outlier = df[(df["age"]<lower_bound)  | (df["age"]>upper_bound)]
print(outlier)

df = df[(df["age"]>=lower_bound) & (df["age"]<=upper_bound)]
df = df.reset_index(drop=True)

print(df.shape)
# Marks
# find the IQR
Q1 = df["marks"].quantile(0.25)
Q3 = df["marks"].quantile(0.75)
IQR = Q3-Q1
print("Q1:",Q1)
print("Q3:",Q3)
print("IQR:",IQR)

# finding conditions for outlier 
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR

print("Lower_Bound:",lower_bound)
print("upper_Bound:",upper_bound)

# detecting outliers 

outlier = df[(df["marks"]<lower_bound)  | (df["marks"]>upper_bound)]
print(outlier)

df = df[(df["marks"]>=lower_bound) & (df["marks"]<=upper_bound)]
df = df.reset_index(drop=True)

print(df.shape)
# Attendance_pct
# find the IQR
Q1 = df["attendance_pct"].quantile(0.25)
Q3 = df["attendance_pct"].quantile(0.75)
IQR = Q3-Q1
print("Q1:",Q1)
print("Q3:",Q3)
print("IQR:",IQR)

# finding conditions for outlier 
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR

print("Lower_Bound:",lower_bound)
print("upper_Bound:",upper_bound)

# detecting outliers 

outlier = df[(df["attendance_pct"]<lower_bound)  | (df["attendance_pct"]>upper_bound)]
print(outlier)

df = df[(df["attendance_pct"]>=lower_bound) & (df["attendance_pct"]<=upper_bound)]
df = df.reset_index(drop=True)
print(df.shape)
print(df.head())
print(df.tail())
print(df.isna().sum())
# df.to_csv("Clean_Full_Practice_dataset_By_using_KNN_Imputer.csv")

# #checking

# df=pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\Clean_Full_Practice_dataset_By_using_KNN_Imputer.csv")
# print(df.isna().sum())
