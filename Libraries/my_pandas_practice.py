import pandas as pd
import numpy as np

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
# df_emp = pd.DataFrame(
#     {
#         "Department": ["HR","IT" , "Finance","Marketing"],
#         "Experience" : [3,5,3,5],
#     },
#     index = ["Emp_A", "Emp_B", "Emp_c","Emp_d"]

# )
# # #1 .loc based selection - Label based 
# # #syntax
# # # df.loc[row_label(s),column_label(s)]
# # print(df_emp.loc["Emp_d", "Department"])
# # print(df_emp.loc["Emp_A":"Emp_d", ["Department"]])

# # #2 . Selection using .iloc (position_based)
# # # syntax 
# # #df.iloc[row_position(s), column_position(s)]
# # print(df_emp.iloc[0,0])
# # print(df_emp.iloc[0:5,0:2])

# # # select employee c using loc 
# # print(df_emp.loc["Emp_c" , "Department" \
# # ""])
# # # select 1st 3 rows and 1 column only
# # print(df_emp.iloc[0:3,0:1])

# #select the experience value of Emp_D using .loc
# # print(df_emp.loc["Emp_d"])
# # #same with iloc 
# # print(df_emp.iloc[3,1])

# # Filtering and Boolean Indexing 
# #Boolean indexing allows you to filter data based on conditions.
# #1. Single Condtion : High earners(salary>55000)
# df = pd.DataFrame(
#     {
#         "Name": ["ALice","bob", "Walium","John"],
#         "Salary": [60000,58900,70000,34500],
#         "Age" : [38,34,37,29]
#     }
# )
# high_earners = df[df["Salary"]>55000]
# print(high_earners)
# #2. Multiple Condtions using bitwise operators : & (AND) , | (OR)
# # Always Wrap each Condition in paraenthese!
# complex_filter = df[(df["Age"]>=30) & (df["Salary"]>60000)]
# print(complex_filter)

# #3. Using .isin() for list matching 
# target_names = df[df["Name"].isin(["ALice", "David"])]
# print(target_names)

# Practice for boolean Filtering 
# store = pd.DataFrame(
#     {
#         "Item": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
#         "Category": [
#             "Electronics",
#             "Accessories",
#             "Accessories",
#             "Electronics",
#             "Accessories",
#         ],
#         "Price": [1200, 25, 45, 300, 80],
#         "Stock": [5, 50, 30, 12, 0],
#     }
# )


# available_stock = store[store["Stock"]>0]
# print(available_stock)
# filtered_store = store[(store["Category"]=="Accessories") & (store["Price"]<50) ]
# print(filtered_store)
# items_filtering = store[store["Item"].isin(["Laptop","Monitor"])]
# print(items_filtering)
# Handling Missing Data 
# df_missing = pd.DataFrame(
    # {
        # "A": [1,2,np.nan,4],
        # "B" : [5,np.nan, np.nan,8],
        # "C": ["x","y","z", None],
    # }
# )
#Detecting missing Values 
# print(df_missing.isna())
#Count missing values per column 
# print(df_missing.isna().sum())
#drop rows with missing values 
# df_dropped = df_missing.dropna()
#fill missing values with a specific constant
# df_filled = df_missing.fillna({"A":df_missing["A"].mean(),"B":0, "C": "Unknown"})
# print(df_filled)
# print(df_missing

# practice
# series
# s = pd.Series([10,20,30,40] , index = ["l" , "bc" , "s" , "wq"])
# print(s)

# # from a list of numbers 
# s = pd.Series([10,20,30,40,50])
# print(s)

# #from a dictionary
# series=pd.Series(
#     {
#         "a": 2,
#         "d": 5,
#         "c": 56,
#         "f": 45,
#     }
# )
# print(series)
# #from one repeated value 
# serie = pd.Series(5, index=["a","b","c","d","f"])
# print(serie)
# # series acts like a numpy array 
# s = pd.Series([10,20,30,40,50])
# print(s)
# print(s.iloc[0])
# print(s[s>20])
# print(s*2)

# #series acts like a dictionary 
# #from a dictionary
# series=pd.Series(
#     {
#         "a": 2,
#         "d": 5,
#         "c": 56,
#         "f": 45,
#     }
# )
# print(series)
# print(series["a"])
# print("a" in series)
# print(series.get("f",0))
# print(series.get("g",0))

# # Math between two  series auto matches by label 
# # This is called alignment. Pandas lines up values by their label name, not their position.
# s1 = pd.Series([1,2,3], index = ["a","b","c"])
# s2 = pd.Series([10,20,30],index= ["b","c","d"] )
# # print(s1+s2)
# print(s1.add(s2, fill_value=0))
# # A series can have a name 
# s = pd.Series([1,2,3] , name = "marks")
# print(s.name)
# print(s)
# dataframe practice

#from a dict
import pandas as pd
import numpy as np
data = {
    "name": ["Ali", "Sara" , "Zain"],
    "marks": [80,90,70],
}
df = pd.DataFrame(data, index = [1,2,3])
print(df)
# Each key becomes a column, each list becomes that column's values.
#from a list of lists

data = [["Ali",80],["Sara",70],["Zain",69]]
df = pd.DataFrame(data , columns=["name" , "marks"])
print(df)

#from a list of tuples 
data = [("Ali",80), ("Sara",78), ("Zain",87)]
df = pd.DataFrame(data,columns=["name","marks"],index = ["a","b","c"])
print(df)

#from a list of dictionaries 
data = [{"name": "Ali" , "marks": 80},{"name":"Sara","marks":78},{"name":"zuhbai", "marks":67}]
df = pd.DataFrame(data,index=["w","y","Z"])
print(df)
# Each dictionary = one row.
# from a series 
s = pd.Series([80,70,90], index = ["ALi","Zain","Sara"], name = "marks")
df = pd.DataFrame(s)
print(df)
# A single Series becomes a DataFrame with one column.
# From a dict of series 
s1 = pd.Series([80,90,40], index = ["ALi","Zain","Sara"] )
s2 = pd.Series([1,2,3], index=["ALi", "Zain","Sara"])
df = pd.DataFrame({"marks":s1 , "rank":s2})
print(df)

# Selecting and Reading Data 
data = {
    "name": ["ALi","Zain","Sara","Nida"],
    "marks": [90,80,70,60],
    "city": ["Lahore","Faisalabad","Karachi","Multan"]
}

df = pd.DataFrame(data, index=[1,2,3,4])
print(df)
#selecting one column 
print(df["name"])
#select multiple Columns 
print(df[["name", "marks"]])
#select a slice of rows
print(df[1:3])
#filter row wirh a condition 
print(df[df["marks"]>70])
#filter with multiple rows
print(df[(df["marks"]>60) & (df["city"]=="Lahore")])
print(df[(df["marks"]>60) | (df["city"]=="Islamabad")])

# Adding  , modifying ,and deleting columns 
df["grade"] = "Pending"
print(df)
# Every row gets "Pending" in the new column.
# Add a new column (calculated from another column)
df["marks_plus_5"] = df["marks"] + 5
print(df)
# Add a column with a condition (Pass/Fail based on marks)
df["result"] = df["marks"]>=60
print(df)
#modify an existing column 
df["marks"] = df["marks"] +3
print(df)
# Delete a column --method 1 del
del df["marks_plus_5"]
print(df)
# delete a column - method 2 pop
removed_col = df.pop("result")
print(df)
print(removed_col)
# Add a column without changing the original  .assign()
df2= df.assign(marks_doubled = df["marks"] * 2)
print(df2)
print(df)
# Handling Missing Data(Nan)
import pandas as pd
import numpy as np

data = {
    "name": ["Ali", "Sara", "Zain", "Nida"],
    "marks": [80, np.nan, 70, np.nan],
    "city": ["Lahore", "Karachi", np.nan, "Lahore"]
}
df_0 = pd.DataFrame(data)
print(df_0)
#chekcing which cells are missing 
print(df_0.isna())
#count how many missing values per column 
print(df_0.isna().sum())
#drop rows that have any missing values 
print(df_0.dropna())
#fill missing values with a fixed value 
print(df_0.fillna(0))
#fill missing values differently per column 
df_0["marks"] = df_0["marks"].fillna(df["marks"].mean())
df_0["city"] = df_0["city"].fillna("unknown")
print(df_0)

# Reading Files in pandas 
import pandas as pd 
data = {
    "name": ["Ali", "Sara", "Zain", "Nida","zarish","asma"],
    "marks": [80, 90, 70, 85,78,56],
    "city": ["Lahore", "Karachi", "Multan", "Lahore","Islamabad", "Rawalpindi"]
   
}
df = pd.DataFrame(data)
df.to_csv("practice.csv", index = False)
#now read it back 
df2 = pd.read_csv("practice.csv")
print(df2)
# peek at just the first few rows
print(df2.head(3))
print(df2.tail())
#Quick summary of the file 
print(df2.info())
print(df2.describe())
print(df2.shape)
print(df2.columns)

#Reading onlu certain columns 
df = pd.read_csv("practice.csv" , usecols = ["name", "marks"])
print(df)
#Reading only a certain numbers of rows
df = pd.read_csv("practice.csv" , nrows=2)
print(df)
#saving a Dataframe back to a file 
df.to_csv("output.csv", index= False)
print(df)