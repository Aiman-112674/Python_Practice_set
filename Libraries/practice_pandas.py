import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\student_dataset_v2.csv")
print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
print(df[df["Age"]>20])

print(df.head)




pivot = pd.pivot_table(df,index="Student ID" , columns = "Gender" , values="Age",aggfunc="mean" )
print(pivot)


females = df[df["Gender"]=="Female"].copy()
females.to_csv('females.csv', index=False)

total_females = len(females)
print("Total:", total_females)



pivot = pd.pivot_table(df,index=["Gender"],values = ["GPA","Attendance Rate (%)",], aggfunc ="mean")
print(pivot)


pivot1=pd.pivot_table(df,index=["Attendance Rate (%)"], values=["Age","GPA"], aggfunc="median")
print(pivot1)


# merge , concat , join , compare

import pandas as pd
marks = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\students_marks.csv")
info = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\students_info.csv")
print(marks.head())
print(marks.shape)
print(info.head())
print(info.shape)

#Query 1: Stack them on top of each other (rows)
combined = pd.concat([marks,info])
print(combined)
print(combined.shape)
combined2 = pd.concat([marks,info], ignore_index=True)
print(combined2)
print(combined2.loc[4,"name"])
print(combined2.loc[4,"subject"])
print(combined2.loc[44,"name"])
#Query 2: Stack them side by side (columns)
combined3 = pd.concat([marks,info],axis=1,ignore_index=True)
print(combined3)
print(combined3.columns)
print(combined2.columns)
#Query 3: merge 
combined4= pd.merge(marks,info, on = "student_id",how = "inner",suffixes=["_marks","_info"])
print(combined4)
# print(combined4.loc[29,"name_marks"])

combined5 = pd.merge(marks,info,on="student_id",how="left",suffixes=["_marks","_info"])
print(combined5)
combined6 = pd.merge(marks,info,on="student_id",how="right",suffixes=["_marks","_info"])
print(combined6)
combined7= pd.merge(marks,info,on="student_id",how="outer", suffixes=["_marks","_info"])
print(combined7)

# Query 4: join
marks_indx = marks.set_index("student_id")
info_indx = info.set_index("student_id")
print(marks_indx.head())
print(info_indx.head())
#by default left joined 
joined = marks_indx.join(info_indx,lsuffix="_marks", rsuffix="_info")
print(joined)
print(joined.shape)

joined_inner = marks_indx.join(info_indx,how="inner", lsuffix="_marks",rsuffix="_info")
print(joined_inner)
print(joined_inner.shape)

joined_outer = marks_indx.join(info_indx,how="outer",lsuffix="_marks",rsuffix="_info")
print(joined_outer)
print(joined_outer.shape)

joined_right = marks_indx.join(info_indx,how="right",lsuffix="_marks",rsuffix="_info")
print(joined_right)
print(joined_right.shape)

# practice on a messy dataset 

df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\messy_students.csv")
print(df)
print(df.dtypes)
#clean the name column first :
df["name"] = df["name"].str.title()
print(df["name"])
df["name"]= df["name"].str.strip()
print(df)

# marks column 

df["marks"] = df["marks"].str.replace("kg","" , regex = False)
df["marks"] = df["marks"].str.replace("marks","" , regex = False)
print(df["marks"])

df["marks"] = df["marks"].replace(["N/A" , "N.A","-"], pd.NA)
print(df["marks"])

#convert to int 
# "coerce" = "just force it, and if it's truly impossible, mark it as missing instead of stopping everything."
df["marks"]= pd.to_numeric(df["marks"],errors = "coerce")
print(df["marks"])
print(df.dtypes)

print(df)

# city 
df["city"] = df["city"].str.strip()
df["city"] = df["city"].str.lower()
print(df)  
print(df.dtypes)


#++++++++++++++++++++++++++++++++++++
# Cleaning the Files using :
# 1. Null Values 
# 2. Duplicated Values
# 3. Wrong Formatted Values 
# 4. Outliers
# Practice is below using Different Files .

# Importing Libraries 
import pandas as pd 
import numpy as np

# Messty_full_Practice_Dataset:
# messy data 
#Loading the dataset
df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\messy_full_practice.csv")
#Printing the 1st 13 rows 
print(df.head(13))
# printing the last 5 rows
print(df.tail())
# checking the number of rows and columns 
print(df.shape)
#calculating the total null values in the entire dataset
print(df.isna().sum())
# calculating the total duplicated values in the dataset
print(df.duplicated().sum())
#Start Cleaning the Dataset 
#First of all , Correcting the Wrong Formated Values 
#Correcting the Column name .
df["name"] = df["name"].str.title()
df["name"] = df["name"].str.strip()
print(df["name"])
# city column 
df["city"] = df["city"].str.title()
df["city"] = df["city"].str.strip()
print(df["city"])
# Handling the Null values in the city column

df["city"] = df["city"].fillna(df["city"].mode()[0])
# marks column  -- correcting the wrong format of values in the marks column
df["marks"] = df["marks"].str.replace("kg", "" , regex=False)
df["marks"] = df["marks"].str.replace("marks", "" , regex=False)
df["marks"] = df["marks"].str.strip()
print(df["marks"])
# converting the dtype of marks which is string to float.
df["marks"]= pd.to_numeric(df["marks"],errors = "coerce")
print(df["marks"])
# Duplicate 
# Finding the duplicated values in the columns 
print(df["name"].duplicated())
print(df["student_id"].duplicated().sum())
(df.drop_duplicates(subset="name" , keep = "last"))
print(df["name"])
# Date formatting -- correcting and maintaining one fixed ISO standard of DateTime in the dataset

df["join_date"] = pd.to_datetime(df["join_date"], format="mixed", errors ="coerce")
df = df.dropna(subset=['join_date'])

# Detecting the Outliers and Cleaning them from Dataset

Q1 = df["marks"].quantile(0.25)
Q3 = df["marks"].quantile(0.75)
# Finding the InterQuartile Range
IQR = Q3-Q1 
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
# Finding the limits to set the condition of outliers
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR

print("lower_bound:",lower_bound)
print("upper_bound:" , upper_bound)

# Detecting the Outliers 
outliers=df[(df["marks"]<=lower_bound) | (df["marks"]>=upper_bound)]
print(outliers)
# Finding the outliers manually 
print(df[df["marks"]>100])
# cleaning the outliers 
df = df[(df["marks"]>=lower_bound) & (df["marks"]<=upper_bound)]
print(df)
# Removing the negative ages from the column Age
df = df[df['age']>0]
print(df)
# Detecting the Outliers in the Column Age 
Q1_age = df["age"].quantile(0.25)
Q3_age= df["age"].quantile(0.75)
# Finding the InterQuartile Range 
IQR_age = Q3_age-Q1_age
print("Q1:", Q1_age)
print("Q3:", Q3_age)
print("IQR:", IQR_age)

# Finding the limits to set the condtions to find Outliers 
lower_bound = Q1_age-1.5*IQR_age
upper_bound = Q3_age+1.5*IQR_age

print("lower_bound:",lower_bound)
print("upper_bound:" , upper_bound)
# Detecting the Outliers 
outliers=df[(df["age"]<=lower_bound) | (df["age"]>=upper_bound)]
print(outliers)
# Removing the Outliers from the Dataset
df = df[(df["age"]>=lower_bound) & (df["age"]<=upper_bound)]
print(df)
# Again checking if still any Null value is present in the dataset 
print(df.isnull().sum())

# resetting the index 

df = df.sort_values("student_id").reset_index(drop=True)
print(df)


## saving the cleaned dataset to a new csv file 
#Before Saving the corrected dataset to a new file makesure the file you are saving only contain the code of the clean dataset 
df.to_csv("Cleaned_the_Messy_Full_Practice.csv", index = False)

#checking 
check = pd.read_csv(r"Libraries\Cleaned_the_Messy_Full_Practice.csv")
print(check.isna().sum())


# 2nd File Cleaning Practice: Employee Salary
# employee salary :
# loading the file 
df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\employee_salaries.csv")
# checking the first 5 rows
print(df.head())
# checking the last  rows 
print(df.tail())
# checking the columns 
print(df.columns)
# getting the detail about the dataset
print(df.info())
# calculating the total null values in the dataset
print(df.isna().sum())
# calculating the duplicated values in the dataset
print(df.duplicated().sum())
# finding the number of rows and columns 
print(df.shape)
# Cleaning the data
# correcting the Age
# removing the negative ages 
df = df[(df["age"]>0)]
print(df)

# detecting and removing the outliers 
# finding the InterQuratile Range
Q1 = df["age"].quantile(0.25)
Q3 = df["age"].quantile(0.75)

IQR = Q3-Q1

print("Q1:",Q1)
print("Q3:",Q3)
print("IQR:",IQR)
# finding the conditions to specify the outliers 
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR

print("Lower Bound:",lower_bound)
print("Upper Bound:" , upper_bound)

#outliers 
outliers = df[(df["age"]<=lower_bound) | (df["age"]>=upper_bound)]
print(outliers)
# cleaning 
df = df[(df["age"]>=lower_bound) & (df["age"]<=upper_bound)]
print(df)

# correcting the salary

# Finding the InterQuartile Range
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)

IQR = Q3-Q1

print("Q1:",Q1)
print("Q3:",Q3)
print("IQR:",IQR)
## finding the conditions to specify the outliers 
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR

print("Lower Bound:",lower_bound)
print("Upper Bound:" , upper_bound)

#outliers 
outliers = df[(df["salary"]<=lower_bound) | (df["salary"]>=upper_bound)]
print(outliers)
# cleaning 
df = df[(df["salary"]>=lower_bound) & (df["salary"]<=upper_bound)]
print(df)

#reset the index 
print(df.reset_index())

# saving the cleaned dataset to a new csv file 
#Before Saving the corrected dataset to a new file makesure the file you are saving only contain the code of the clean dataset . 

df.to_csv("Employee_Salaries_Cleaned.csv",index=False)
#checking 
check = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\Employee_Salaries_Cleaned.csv")
print(check.isna().sum())


# ecommerce_oders messy data 
import pandas as pd
import numpy as np 

df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\ecommerce_orders.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.info())

print(df.isna().sum())
print(df.duplicated().sum())

# Correcting the wrong formatted city column 
df["customer_city"]=df["customer_city"].str.strip()

df["customer_city"]=df["customer_city"].str.title()
# replace the NAN value 
df["customer_city"] = df["customer_city"].fillna(df["customer_city"].mode()[0])
print(df["customer_city"])
# checking the null values of this column 
print(df["customer_city"].isna().sum())

#Correcting the wrong formatted status column 

df["status"]=df["status"].str.strip()
df["status"]=df["status"].str.title()
#replacing the Null values 
df["status"]=df["status"].fillna(df["status"].mode()[0])
#checking for Null values in this column 
print(df["status"].isna().sum())
print(df["status"])

# Correcting the Price column 

print(df["price"])
# correcting the wrong formatted values
df["price"] = df["price"].str.replace("rs","",regex=False)
# changing the dtype of price column which is string but it need to be float
df["price"] = pd.to_numeric(df["price"], errors="coerce")
# checking the null values in the price column 
print(df["price"].isna().sum())
#replacing the null values with the mean of the price column values 
df["price"]= df["price"].fillna(df["price"].mean())
#again checking the null values 
print(df["price"].isna().sum())
#printing the price column 
print(df["price"])
# detecting and removing Outliers

Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)

# finding the InterQuartile Range 

IQR = Q3-Q1
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

#Finding the limits to set the conditions for detecting the outliers 

lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR

print("Lower_bound:",lower_bound)
print("Upper_bound:", upper_bound)

# Detecting the Outliers

outliers = df[(df["price"]<=lower_bound) | (df["price"]>=upper_bound)]
print(outliers)

# Cleaning the outlier 
df = df[(df["price"]>=lower_bound) & (df["price"]<=upper_bound)]
print(df)


# Quantity Column 

df["quantity"] = df["quantity"].str.replace("units","", regex=False)
df["quantity"] = pd.to_numeric(df["quantity"],errors="coerce")
df = df[(df["quantity"]>0)]
print(df)
print(df["quantity"].isna().sum())

# print()

# checking any null and duplicated value 

print(df.isna().sum())
print(df.duplicated().sum())
print(df.dtypes)

# duplicated 
print(df.duplicated().sum())
df=(df.drop_duplicates(keep="first"))
print(df)

#saving the correct or clean df

# df.to_csv("Ecommerce_Orders_Clean.csv", index=False)

# #checking 

df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\Ecommerce_Orders_Clean.csv")
print(df.isna().sum())
print(df)

