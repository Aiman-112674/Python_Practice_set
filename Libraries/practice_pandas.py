
import pandas as pd
import numpy as np
# df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\student_dataset_v2.csv")
# print(df.head())
# print(df.info())
# print(df.shape)
# print(df.describe())
# print(df[df["Age"]>20])

# print(df.head)




# pivot = pd.pivot_table(df,index="Student ID" , columns = "Gender" , values="Age",aggfunc="mean" )
# print(pivot)


# females = df[df["Gender"]=="Female"].copy()
# females.to_csv('females.csv', index=False)

# total_females = len(females)
# print("Total:", total_females)



# pivot = pd.pivot_table(df,index=["Gender"],values = ["GPA","Attendance Rate (%)",], aggfunc ="mean")
# print(pivot)


# pivot1=pd.pivot_table(df,index=["Attendance Rate (%)"], values=["Age","GPA"], aggfunc="median")
# print(pivot1)


# merge , concat , join , compare

import pandas as pd
# marks = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\students_marks.csv")
# info = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\students_info.csv")
# print(marks.head())
# print(marks.shape)
# print(info.head())
# print(info.shape)

# #Query 1: Stack them on top of each other (rows)
# combined = pd.concat([marks,info])
# print(combined)
# print(combined.shape)
# combined2 = pd.concat([marks,info], ignore_index=True)
# print(combined2)
# print(combined2.loc[4,"name"])
# print(combined2.loc[4,"subject"])
# print(combined2.loc[44,"name"])
# #Query 2: Stack them side by side (columns)
# combined3 = pd.concat([marks,info],axis=1,ignore_index=True)
# print(combined3)
# print(combined3.columns)
# print(combined2.columns)
# #Query 3: merge 
# combined4= pd.merge(marks,info, on = "student_id",how = "inner",suffixes=["_marks","_info"])
# print(combined4)
# # print(combined4.loc[29,"name_marks"])

# combined5 = pd.merge(marks,info,on="student_id",how="left",suffixes=["_marks","_info"])
# print(combined5)
# combined6 = pd.merge(marks,info,on="student_id",how="right",suffixes=["_marks","_info"])
# print(combined6)
# combined7= pd.merge(marks,info,on="student_id",how="outer", suffixes=["_marks","_info"])
# print(combined7)

# Query 4: join
# marks_indx = marks.set_index("student_id")
# info_indx = info.set_index("student_id")
# print(marks_indx.head())
# print(info_indx.head())
# #by default left joined 
# joined = marks_indx.join(info_indx,lsuffix="_marks", rsuffix="_info")
# print(joined)
# print(joined.shape)

# joined_inner = marks_indx.join(info_indx,how="inner", lsuffix="_marks",rsuffix="_info")
# print(joined_inner)
# print(joined_inner.shape)

# joined_outer = marks_indx.join(info_indx,how="outer",lsuffix="_marks",rsuffix="_info")
# print(joined_outer)
# print(joined_outer.shape)

# joined_right = marks_indx.join(info_indx,how="right",lsuffix="_marks",rsuffix="_info")
# print(joined_right)
# print(joined_right.shape)

# practice on a messy dataset 

df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Libraries\messy_students.csv")
print(df)
print(df.dtypes)
#clean the name column first :
df["name"] = df["name"].str.title()
print(df["name"])
df["name"]= df["name"].str.strip()
print(df)

#marks column 

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
