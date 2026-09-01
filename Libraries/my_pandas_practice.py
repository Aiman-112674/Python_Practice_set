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
s = pd.Series([10,20,30,40] , index = ["l" , "bc" , "s" , "wq"])
print(s)

# from a list of numbers 
s = pd.Series([10,20,30,40,50])
print(s)

#from a dictionary
series=pd.Series(
    {
        "a": 2,
        "d": 5,
        "c": 56,
        "f": 45,
    }
)
print(series)
#from one repeated value 
serie = pd.Series(5, index=["a","b","c","d","f"])
print(serie)
# series acts like a numpy array 
s = pd.Series([10,20,30,40,50])
print(s)
print(s.iloc[0])
print(s[s>20])
print(s*2)

#series acts like a dictionary 
#from a dictionary
series=pd.Series(
    {
        "a": 2,
        "d": 5,
        "c": 56,
        "f": 45,
    }
)
print(series)
print(series["a"])
print("a" in series)
print(series.get("f",0))
print(series.get("g",0))

# Math between two  series auto matches by label 
# This is called alignment. Pandas lines up values by their label name, not their position.
s1 = pd.Series([1,2,3], index = ["a","b","c"])
s2 = pd.Series([10,20,30],index= ["b","c","d"] )
# print(s1+s2)
print(s1.add(s2, fill_value=0))
# A series can have a name 
s = pd.Series([1,2,3] , name = "marks")
print(s.name)
print(s)
# dataframe practice
data = {
    "name": ["Aiman","Sara"],
    "Age": [25,30],
}

df = pd.DataFrame(data)
print(df)
# df from a list of dictoinaries 
df_1 = pd.DataFrame([
    {
        "a":1,
        "n":2,
    },
    {
        "a":4,
        "n":6,
    }

])

print(df_1)
#from a dict of series 
df_2 = pd.DataFrame({
    "one": pd.Series([1,2,3] , index = ["x", "y","z"]),
    "two": pd.Series([4,5,6], index = ["x", "y","z"])
})
print(df_2)
