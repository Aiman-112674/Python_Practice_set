#Numpy
# NumPy (short for Numerical Python) is the core library for scientific computing, data analysis, and machine learning in Python.
import numpy as np
# What is an Array?
# The core building block of NumPy is the ndarray (n-dimensional array). Unlike Python lists, NumPy arrays can only hold one data type (usually numbers), which allows them to run at C-speed.

#creating 1 dimentional array
arr_1 = np.array([[1,2,3,4] , [5,6,7,8]])
print(arr_1)
a = np.array([2,3,4])
print(a)
b = np.array([3,4,5])
print(b)
c = a*b
print(c)
#checking the shape of array 
print(a.shape)
#checking the dimension
print(a.ndim)
# checking the size
print(a.size)
#checking the data  type
print(b.dtype)
#checking the tyoe
print(type(a))

d = np.arange(15)
d.reshape(3,5)
print(d)

# 2 or 3 dimenstional arrays  (3,4) 1st is the number of rows and 2nd is the number of columns 
#filled with zeros or ones (pass shape as a tuple)
print(np.zeros((3,4)))
print(np.ones((2,3,4)))   #2 is the number of time the arrays to create like craete 2 arrays and 3 rows and 4 columns
print(np.empty((2,3)))

# 1D Array (Vector): A single row of numbers.

# 2D Array (Matrix): Rows and columns (like a spreadsheet).

# 3D Array (Tensor): A stack of matrices (like a cube of numbers).

a = np.arange(6)  # 1d array
print(a)

c = np.arange(12).reshape(2,6)  #2d array
print(c)

d = np.arange(24).reshape(2,3,4)  #3d array
print(d)

# Basic operations on arrays 

x = np.array([20,30,40,50])
y = np.arange(4)
z = x-y
print(z)

w = y**2
print(w)

q= 2*x
print(q)

s = x+y
print(s)

#sequence of numbers 
range_arr = np.arange(0,12,2)  #(Start, Stop, Step) its same as python range function
print(range_arr)
linear_arr = np.linspace(0,1,5)   ## 5 numbers evenly spaced between 0 and 1
print(linear_arr)
#random numbers 
rand_matrix = np.random.rand(2,2)
print(rand_matrix)

#Array Indexing and Slicing 
#Extracting elements works like Python lists, but with extra superpowers for multi-dimensional data.
#1D slicing
a = np.array([10,20,30,40,50])
print(a[1:4])
print(a[2:5])
# 2D slicing   
matrix = np.array([[10,20,30] , [40,50,60] , [70,80,90]])
print(matrix[0,1])
print(matrix[:,0])
# Step 1: Understand the 2D SyntaxWhen slicing a matrix in NumPy, the syntax inside the brackets is always split by a comma:$$\text{matrix}[\mathbf{\text{Row Slicing}}\,,\, \mathbf{\text{Column Slicing}}]$$Everything before the comma controls which rows you pick.Everything after the comma controls which columns you pick.

print(matrix[0:2 , 1:3])
print(matrix[1:3,0:2])
print(matrix[0:3,1:2])

# Reshape the array 
arr = np.arange(1,7)
print(arr)
#reshape 1D to 2D
matrix = arr.reshape(2,3)
print(matrix)
#flatten 2D back to 1D 
flat = matrix.flatten()
print(flat)

# Vectorization & operations 
#Vectorization lets you perform math on an entire array at once without writing for loops.

#basic arithematic 
x = np.array([1,2,3,4])
y = np.array([9,8,7,6])
print(x+y)
print(x*y)
print(x/y)
# Boolean Filtering(Masking)

scores = np.array([45,88,92,30,71])
passed = scores>=50
print(passed)
print(scores[passed])

# Broadcasting rules 
#Broadcasting allows NumPy to perform math between arrays of different shapes. NumPy automatically stretches the smaller array across the larger one.
matrix = np.array([[1,2,3], [4,5,6]])  # Shape: (2, 3)
vector = np.array([10,20,30])    # Shape: (3,)
# The vector gets added to EACH row of the matrix automatically
result = matrix + vector
print(result)

# Aggregations & Axis Operations 
# Functions like sum, mean, max, and min can run across the entire array or along a specific axis:

# axis=0: Collapse down the columns (vertical).

# axis=1: Collapse across the rows (horizontal).

data = np.array([[1,2] , [3,4]])
print(np.sum(data))  # Output: 10 (Total sum)
print(np.sum(data,axis=0))  # Output: [4, 6] (Sum of each column)
print(np.sum(data,axis=1))   # Output: [3, 7] (Sum of each row)
print(np.mean(data))    # Output: 2.5

# stacking and splitting Arrays 
#Combining separate arrays together or breaking them down:

a = np.array([1,2])
b = np.array([3,4])

#vertical stacking (row-wise)
v_stacked = np.vstack((a,b))
print(v_stacked)

# Horizontal Stacking (Column-wise)
h_stack= np.hstack((a,b))
print(h_stack)

# view vs copy
# In NumPy, slicing creates a View. A view is just a window looking at the original array memory. If you modify a view, you permanently change the original array.

orignal = np.array([1,2,3,4,5])
print(orignal)
#slice the array , create a view not a copy
view_slice = orignal[1:4]
print(view_slice)
#modify element 0 of the view
view_slice[0] = 89
#the original array was changed 
print(orignal)
#How to make an independent Copy instead 
safe_copy = orignal[1:4].copy()
print(safe_copy)
safe_copy[0] = 67 #Leaves original untouched 
print(safe_copy)

#Adding new axes
# Sometimes you have a 1D vector shape (6,) but a function (or model) expects a 2D matrix shape like (1, 6) or (6, 1).
# 1.Method:np.newaxis
a =np.array([1,2,3,4,5,6])
print(a)
row_vec = a[np.newaxis, :1]
print(row_vec.shape)





#unique Values & Counts (np.unique)
data = np.array([11,12,11,13,12,14,15,16,11,17,12,11,18,19,13,11,12])
uniques , first_indcies , counts = np.unique(
    data , return_index = True , return_counts = True
)
print(uniques)
print(counts)

# Transposing matrics (.T and np.transpose)
# Transposing flips a matrix over its diagonal—turning its rows into columns and columns into rows.
matrix = np.array([[1,2,3],[4,5,6]])  #shape (2,3)
#transpose shortcut
flipped = matrix.T
print(flipped)

# Saving and loading data 
#NumPy provides built-in methods to save array data directly to your disk so you don't lose calculated results
arr = np.array([1,2,3,4,5,6])
np.save("my_array.npy" , arr)
#load array back into python 
loaded_arr = np.load("my_array.npy")
#save to a text / csv file 
np.savetxt("data.csv" , arr, delimiter = ",")

# Reverse an Array 
# Reversing 1D vectors or 2D matrices is done using np.flip().

# 1D Arrays: Reverses the entire array end-to-end.

# 2D Arrays: You can choose to reverse rows only, columns only, or both using the axis parameter.
#1d
arr = np.array([1,2,3,4,5])
reversed_arr = np.flip(arr)
print(reversed_arr)

#2d

matrix = np.array([[1,2],[3,4]])
#reverse only along rows (flip top-to-bottom)
print(np.flip(matrix, axis=0))
#reverse only along columns 
print(np.flip(matrix, axis=1))
