import pandas as pd

# # The two core building blocks
# # 1. Series — a single column of data

# # Think of a Series as one column from a spreadsheet — a list of values, but each one also has a label (called an index) attached to it.
# ages = pd.Series([21,25,19,30,34,23,25])
# print(ages)
# #indexing 
# ages = pd.Series([21,25,4], index = ["Aiman", "Faiqa" , "Hareem"])
# print(ages)
# import numpy as np

# s = pd.Series([1,3,4,np.nan,6,8])
# print(s)


# cities = pd.Series([3000000,5000000,6000000,4000000], index = ["Isalamabad", "Lahore","Multan", "Faisalabad"])
# print("Popular Cities")
# print(cities)


# # 2. DataFrame — a full table (multiple columns together)

# # This is the big one — a DataFrame is like an entire spreadsheet: multiple columns, each one basically a Series, all lined up together sharing the same row labels.

# data = {
#     "Name": ["Aiman","Ali" , "Sara"],
#     "Age": [21,25,19],
#     "city": ["Faisalabad","Lahore","Karachi"]

# }
# df = pd.DataFrame(data)
# print(df)

# products = {
#     "Product_Name": ["Facewash","Sunblock","Moisturezier","Blush", "Serum","Lip_Pencil", "Gloss"],
#     "Price" : [500,1000,800,500,1600,100,300],
#     "InStock": ["yes","yes","no" , "yes","no","yes","no"]

# }
# df = pd.DataFrame(products)
# print("Products")
# print(df)

# #Quick Summary 
# print(df.info())
# print(df.describe())

# # Viewing data from start
# print(df.head(2))

# #viewing data from last
# print(df.tail(3))
# # checking the shape
# print(df.shape)
# #checking the columns
# print(df.columns)

# #Selection , Indexing & Slicing 
# #.loc
# #.iloc
# #dataframe 
df_emp = pd.DataFrame(
    {
        "Department": ["HR","IT" , "Finance","Marketing"],
        "Experience" : [3,5,3,5],
    },
    index = ["Emp_A", "Emp_B", "Emp_c","Emp_d"]

)
# #1 .loc based selection - Label based 
# #syntax
# # df.loc[row_label(s),column_label(s)]
# print(df_emp.loc["Emp_d", "Department"])
# print(df_emp.loc["Emp_A":"Emp_d", ["Department"]])

# #2 . Selection using .iloc (position_based)
# # syntax 
# #df.iloc[row_position(s), column_position(s)]
# print(df_emp.iloc[0,0])
# print(df_emp.iloc[0:5,0:2])

# # select employee c using loc 
# print(df_emp.loc["Emp_c" , "Department" \
# ""])
# # select 1st 3 rows and 1 column only
# print(df_emp.iloc[0:3,0:1])

#select the experience value of Emp_D using .loc
# print(df_emp.loc["Emp_d"])
# #same with iloc 
# print(df_emp.iloc[3,1])

# Filtering and Boolean Indexing 
#Boolean indexing allows you to filter data based on conditions.
#1. Single Condtion : High earners(salary>55000)
df = pd.DataFrame(
    {
        "Name": ["ALice","bob", "Walium","John"],
        "Salary": [60000,58900,70000,34500],
        "Age" : [38,34,37,29]
    }
)
high_earners = df[df["Salary"]>55000]
print(high_earners)
#2. Multiple Condtions using bitwise operators : & (AND) , | (OR)
# Always Wrap each Condition in paraenthese!
complex_filter = df[(df["Age"]>=30) & (df["Salary"]>60000)]
print(complex_filter)

#3. Using .isin() for list matching 
target_names = df[df["Name"].isin(["ALice", "David"])]
print(target_names)