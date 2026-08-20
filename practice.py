# ++++++++++++++++++++++++++++++++
#Python Practice 

# print("Hello World")
# name="Aiman" ;
# name1 = "Software Engineer"
# print(name , name1)

# age = 30
# marks = 40.0 
# class1 = "BSSE"

# print(class1)

# ++++++++++++++++++ Operators 


# Arithematic Operator (+,-,/,*,**,%)

# x=5
# y=10
# z = x+y*2
# print(z)

# Comparsion/Relational operator  (==,!=,>,<,>=,<=)
# x = 6
# y = 16 
# print(x==y)
# print(x>=y)

# Assignment operator  (x+=y,-=,/=,*=,**=,%=,=)
# x = 5
# y = 18 
# x-=y
# print(x)

# Logical Operator 

# x = True 
# y = False
# print(x and y)

# # # Conversion 
# # Two type of conversion in pyhton 
# # 1) auto 
# # 2) manual 


# # Autoo Conversion
# x = 5
# y = 10.5
# z = x+y 
# print(type(z))

# # Manual Conversion

# x = "5"
# y=int(x)
# print(y)
# print(type(y))


# Input Function --- use to take input from user . it only take inputs in the form of strings , to take it  as number its important to convert it into int 

# Task 1  --- Marks system 
# input function
# name = input("Enter your  first name  : " )
# name1 = input("Enter your  last name  : "  )
# classname =  input("Enter your Class name : ")
# marks = input(("Enter your English marks : "))
# marks1 = input("Enter your Math marks : ")
# marks2 = input("Enter your physics marks : ")
# marks3 = input("Enter your Computer marks : ")
# total_marks = int(input("Enter your Total Marks : "))

# obtained_marks =int(marks) + int (marks1) + int(marks2) + int(marks3)

# print(f"Total Marks are : {total_marks} ,  Your Obtained Marks are these {obtained_marks}")
# percentage_of_marks = obtained_marks / total_marks * 100
# print(f"Percentage_of_marks : {percentage_of_marks}")


# Task 2 --- Calculator


# try:
#     number0 = int(input("Enter 1st number : "))
#     number1 = int(input("Enter 2nd number (Enter Zero if not) : "))
#     choice = input("Enter the operation you want to perform : + / - / // / * / % / square / cube  ")
#     if(choice == "+"):
#         sum_0 = number0+number1
#         print(sum_0)
#     elif(choice== "-"):
#         substrct_0 = number0-number1
#         print(substrct_0)
#     elif(choice == "//"):
#         divide_0 = number0//number1
#         print(divide_0)
#     elif(choice == "*"):
#         multiplication_0 = number0*number1
#         print(multiplication_0)
#     elif(choice=="%"):
#         reminder_0 = number0%number1
#         print(reminder_0)
#     elif(choice == "square"):
#         square_0 = number0 ** 2 
#         print(square_0)
#     elif(choice=="cube"):
#         cube_0 = number0**3
#         print(cube_0)
#     else:
#         print("You Enter Invalid Operator . \n Try again.")
# except ValueError:
#     print("Invalid Input . Please enter Whole number only")
# except ZeroDivisionError:
#     print("You Cannot divide by Zero.")


# practice

# if-elif-else 
# example 1
# age=12
# if age<=17:
#     print("You are under age.")
# else:
#     print("You are over age . ")

# exmaple2
# age = int(input("Enter Your Age :  "))
# if age>=20:
#     print("You are Over Age .")
# else :
#     print("You are Under Age . ")

# example3 
# And operation

# marks_percentage = int(input("Enter your marks percentage: "))
# if marks_percentage>=80 and marks_percentage<=90:
#     print("Your Grade is A.")
# elif marks_percentage>=70 and marks_percentage<80:
#     print("Your Grade is B.")
# elif marks_percentage>=60 and marks_percentage<=70:
#     print("Your Garde is C.")
# else:
#     print("Your Garde is F.")

# OR operation 

# marks_percentage = int(input("Enter your marks percentage: "))

# if marks_percentage>=80 or marks_percentage>=90:
#     print("Your Grade is A.")
# elif marks_percentage>=70 or marks_percentage>=80:
#     print("Your Grade is B.")
# elif marks_percentage>=60 or marks_percentage>=70:
#     print("Your Garde is C.")
# else:
#     print("Your Garde is F.")
  
#+++++++++++++++++++++++++ Strings & its  Functions 

# Strings ("",'',''')
# string is immutable / not update / cannot change after declaration 

# name_0 = "We are Muslims \n We live in Pakistan."
# name_1 = "We are Muslims\t We live in Pakistan."

# print(name_0 ) 
# print(name_1)


# Replacing

# name_3= "we are muslims"  #white spaces within the sentenes also indexed in memory
#  name_3[0]= "A"   #not possible to replace the strings or update after declaration 

# print(name_3[0])
# print(name_3[1])
# print(name_3[2])
# print(name_3[3])
# print(name_3[4])

# name = "Aiman"
# age = "12"

# print("My name is " +  name  +   " My Age is: " + age)

# print(len(age))

# name = "we are muslims"
# print(name.upper())
# print(name.lower())

#Replacing the strings -- means creating a new strings for temporary , does not change the existing string 

# print(name.replace("muslims" , "pakistan")) # this will print we are pakistan 
# print(name)   #this will print we are muslims 

#finding the index of a character 

# print(name.index("l"))
# print(name.index("r"))

#Slicing in python 
  # compiler read the instructions from left side and line by line 
#Positive Slicing 
   # 0 -- represent the starting indexing  , 6 -- represent the ending index in +ve slicing 
# print(name[0:6])
# print(name[0:2])
# print(name[0:1])
# print(name[0:])
# print(name[5:])
# print(name[0:5])

# #Negative Slicing 
# we are muslims 
# print(name[-1:])
# print(name[-2:])
# print(name[-5:])
# print(name[-7:])
# print(name[-11:])
# print(name[-14:])
# print(name[-14:-1])  
# #-14 --  represent ending indexing  , -1 --- represent starting indexing in the -ve slicing 

# print(name[-14:-2])
# print(name[-14:-3])
# print(name[-14:-4])
# print(name[-14:-5])
# print(name[-14:-6])
# print(name[-14:-7])
# print(name[-14:-8])
# print(name[-14:-9])
# print(name[-14:-10])
# print(name[-14:-11])
# print(name[-14:-12])
# print(name[-14:-13])
# print(name[-14:-14])

# new example for slicing 
# self = "aiman zafar "
# print(self)

# a i m a n _ z a f a r _  --string
# 0 1 2 3 4 5 6 7 8 9 10 11  -- indexing include white spaces

#positive slicing 

# print(self[0:2])
# print(self[0:5])
# print(self[0:])
# print(self[:7])

#negative slicing 
# print(self[-5:-1])
# print(self[-8:-2])
# print(self[-7:-1])
# print(self[-6:-1])
# print(self[-11:-4])
# print(self[-12:-5])

#Capitalize --only the first word of the sentence 

# print(name.capitalize())
# print(self.capitalize())

#Title  -- Capitalize the every first character of a word in the sentence 

# print(name.title())
# print(self.title())

#Count -- count the time a specific alphabet or character (given in as argument) shown in the sentence 

# print(self.count("a"))
# print(self.count("r"))
# print(name.count("r"))
# print(name.count("m"))

#Startswith -- check if the sentence declared with the given argument 

# print(self.startswith("aiman"))
# print(name.startswith("are"))
# print(name.startswith("muslims"))
# print(self.startswith("za"))

#Endswith --- check if the declared sentence end with the given argument 

# print(self.endswith("aiman"))
# print(self.endswith("zafar "))
# print(name.endswith("we"))
# print(name.endswith("ms"))

#Split in python 

# print(name.split(" "))
# print(self.split(' '))

#Strip --- remove the white spaces 
# name_0 = "      sania      "
# self_0 = "      aiman     "
# print(self_0.strip())
# print(name_0.strip())

#LStrip -- left strip 

# print(name_0.lstrip())
# print(self_0.lstrip())

#RStrip -- Right strip 

# print(name_0.rstrip())
# print(self_0.rstrip())

# Finding a specific character in the sentence like finding its index by giving that specific character as a argument 

# print(self.find("m"))
# print(name.find("i"))

#Task 3 ++++++++++++++ ATM Machine 

# balance = 10000
# choice = input("Enter the Operation you want to perform : deposit / withdraw /check  " )

# if choice == "deposit":
#     deposit = int(input("Enter the Amount of money you want to add to the current balance : "))
#     balance = balance+deposit
#     print(f"Your remaining current balance is {balance}")
# elif choice == "withdraw":
#      withdraw = int(input("Enter the Amount of money you want to withdraw  : "))
#      if balance<withdraw:
#          print("Insufficent money . please deposit first")
#      elif balance>= withdraw:
#          balance = balance-withdraw
#          print(f"Your remaining current balance is {balance}")
# elif choice == "check":
#     print(f"Your Current Balance is {balance}")
# else:
#     print(f"Your Current Balance is {balance}")
# print("Transaction done ")
 

# Task 4 ++++++++++++++++ Even - odd checker 

# # number = int(input("Enter the Number(you want to check: )"))
# # if (number%2==0 ):
# #     print(f"The Number you entered is Even {number}")
# # elif (number%2 !=0):
# #     print(f"The Number you entered is odd {number}")
# # else:
# #     print("Please enter a complete whole Number. \n Try Again.")

# # List in Python 
# # List is mutable this means there value can be change .
# # why : list store multiple datatypes , so instead to create multiple variables , we can store all Vars in one list 

# #Indexing in list start from zero 

# marks = [9 , 67.9 , "Aiman" , 233 , 3.44]
# print(marks)                  # Prints the complete list
# print(type(marks))              # Shows the data type (list)
# print(len(marks))                # Returns total number of elements        

# print(marks[4])                   # Access element at index 4
#     # As Lists are Mutable so 1st we access the index and then after checking whats at that index 
#     # we change or update or modified that index with value Faiqa 

# marks[4] = "Faiqa"
# print(marks)

#  Difference between 
# # Strings vs Lists 

# # Strings are Immutable 
# # Immutable means there values cannot be changed
# #example 
# str = "hello"
# print(str)
# print(str[0])   # output --h 
# # str[0] = "y"    # error bcz string cannot be modified 


# # Lists are Mutable 
# # Mutable means their Values can be Changed 
# #Exampel 

# student = ['Zainab' , 'Laraib' , 'Wajiha' , 89]  
# print(student[3])    # output -- 89 

# student[3] = "Ratiya"        # Change the 89 value with Ratiya 
# print(student)

# These changes in Lists are Permanent 

# List Slicing 

# list = ['ali' , 'raza' , 89 , 76.8 , 33 , 33.2]

# Positive slicing 

# print(list[0:5])
# print(list[1:])
# print(list[0:])

# [0:5] -- it startt from 0 and end at 5 but does not include the 5 in printing , it just print 0-4

# Negative Slicing 


# list = ['ali' , 'raza' , 89 , 76.8 , 33 , 33.2]

# print(list[-3:-1])
# print(list[-4:-1])
# print(list[-5:-1])
# print(list[-6:-1])
# print(list[-6:])
# print(list[:-1])


# [-3:-1]  -- -3 this is the ending index and its include means the value at this index is included and -1 is the starting index and its value is not included 

# List Methods 

# list_1 = [4,3,2,1,6,7,8]

#append() -- for adding a new value at the end of list 

# list_1.append(7)
# print(list_1)

# list_1.append(10)
# print(list_1)

# list_1.append('Aiman')
# print(list_1)

# sort() 
# sort list in ascending order by default
# list_2 = [5,2,1,8,9,10]
# list_2.sort()
# print(list_2)

# list_2.sort(reverse=True)
# sorts list in descending order .

# print(list_2)

# reverse()
# reverse the current order only . 
# list_2.reverse()
# print(list_2)

# Inseration 
# Insert (index, value) -- inserts an element at any position .
# list_2.insert(7,11)
# print(list_2)
# list_2.insert(8,12)
# print(list_2)

#remove -- remove(value)
# # in this method as argument the value is to be provide that we need to remove from the list 
# list_2.remove(5)
# print(list_2)
# 5 deleted 

# Pop --pop(index) 
# pop is also used for removing a value but it takes index as argument not the value as we did in remove

# list_2.pop(2)
# print(list_2)
# it remove the index 2 which stores the value 8 . 

#Task 5+++++++++++ Grading Task 

# input function
# name = input("Enter your  first name  : " )
# name1 = input("Enter your  last name  : "  )
# classname =  input("Enter your Class name : ")
# marks = int(input(("Enter your English marks : ")))
# marks1 = int(input("Enter your Math marks : "))
# marks2 = int(input("Enter your physics marks : "))
# marks3 = int(input("Enter your Computer marks : "))
# list_marks = [ marks , marks1 , marks2  , marks3 ]
# total_marks = int(input("Enter your Total Marks : "))

# obtained_marks =int(sum(list_marks))
# print(obtained_marks)

# print(f"Total Marks are : {total_marks} ,  Your Obtained Marks are these {obtained_marks}")
# percentage_of_marks = obtained_marks / total_marks * 100
# print(f"Percentage_of_marks : {percentage_of_marks}")

# if percentage_of_marks>80 and percentage_of_marks<=90:
#     print("Your Obtained Grade is A")
# elif percentage_of_marks>70 and percentage_of_marks<=80:
#     print("Your Obtained Grade is -A")
# elif percentage_of_marks>60 and percentage_of_marks<=70:
#     print("Your Obtained Grade is B")
# elif percentage_of_marks>50 and percentage_of_marks<=60:
#     print("Your Obtained Grade is C")
# else:
#     print("Your Obtained Grade is F")


#+++++++++++++ Tuple 
#Tuple are Immutable , means they cannot modified and changed 
# once created , they cannot be changed 
# ()

# tup = (2,3,1,3,1,2,6,7)
# print(tup)
# print(type(tup))

# t = ('aiman') ; t_0 = ("aiman" , ) #now its datatype is string , but i expected to be tuple bcz of () , so for tupple we need to 
#                #add a , if only one variable is currently in the tuple like ('aiman',)
# print(type(t))
# print(type(t_0))

# # accesing the value using index
# print(tup[2])
# print(tup[0])
# Error bcz tuple are immutable
# tup[0] = 5 
# print(tup[0])

#Tuple Slicing

# tup = ("Aiman" , "Faiqa" , "67.6" , "83.4")

# #Positive SLicing 

# print(tup[0:3])
# print(tup[0:])

# #Negative SLicing 

# print(tup[-3:-1])
# print(tup[-4:])
# print(tup[:-1])


# Tuple Methods 

# index() - returns the index of the first occurrence 
# tup = (2,3,4,1,1,4)
# print(tup.index(4))  #index 2 bcz 4 is 2 times 
# print(tup.index(3))

# #index in tuple takes only value 

# # count -- how many times a value appear

# print(tup.count(1))

#++++++++++++++++++ Dictionary
# Dictionary --in Python is a built-in data type that stores data as key-value pairs 
# {}
# Dict is mutable --it means we can change the data after creation 
# student = {
#     "name" : "Aiman" , 
#     "Age" : 22 , 
#     "city" : "Faisalabad"
# }
# print(student)

#Mutable 
# print(student["Age"])
# student["Age"] = 17
# print(student["Age"])


# pop() --- remove the specified key and returns its value .

# print(student.pop("Age"))
# print(student)  # for confirming that pop remove the age variable

# Popitem -- remove and returns the last inserted  key_value pair .

# print(student.popitem())
# print(student)  # to confirm popitem remove this last city variable 


# Clear ----reomve all the items from the dictionary 

# student.clear()
# print(student)  #confirming if the dict is now empty or not 

# Copy - creates a copy of the dictionary

# new_student = student.copy()
# print(new_student)  # to confirm that the new_student copy or not

# setdefault --- 
#return the value of the key 
# if the key does not exist , it adds the key 
# with the given default value 
# student = {
    # "name" : "Aiman" , 
    # "Age" : 22 , 
    # "city" : "Faisalabad"
# }


# print(student.setdefault("Subject" , "Software Enginnering"))
# print(student)  #to confirm that the subject key and its value is store permanently in the dict 

# fromkeys()
# create a new dictionary using given keys 
# and assigns the same value to all the keys 

# keys = ("name" , "age" , "city") 
# new_dict = dict.fromkeys(keys , "Not Given")
# print(new_dict)
#fromkeys -- can only assign same value to the keys not different values
#zip -- for creating dict with different keys and values 

# keys_0 = ("name" , "age")
# values = ("Aiman" , "22")
# new_dict_0 = dict(zip(keys_0 , values ))
# print(new_dict_0)

#Practice
#  ++++++++++++++++++++ Student Report Card


# Student Report Card
#marks
# name = input("Enter your name: ")
# classname = input("Enter your class: ")
# eng_marks = int(input("Enter your English Marks: "))
# maths_marks = int(input("Enter your Maths Marks: "))
# phy_marks = int(input("Enter your Physics Marks: "))
# chem_marks = int(input("Enter your Chemistry Marks: "))
# bio_marks = int(input("Enter your Biology Marks: "))
# total_marks = int(input("Enter  Your Total Subject Marks: "))
# marks_list = [eng_marks,maths_marks,phy_marks,chem_marks,bio_marks]
# obtained_marks = sum(marks_list)
# print(obtained_marks)
# percentage = obtained_marks / total_marks * 100 

# print(f"Your Total Subject marks are {total_marks}  and your Obtained marks are {obtained_marks} \n Percentage of your Obtained marks are {percentage}")
# # Grading 
# if percentage>90 and percentage<=100:
#     print(f"Your Percentage is {percentage} , So Your Grade is +A .")
# elif percentage>80 and percentage<=90:
#     print(f"Your Percentage is {percentage}  , So Your Garde is B .")
# elif percentage>70 and percentage<=80:
#     print(f"Your Percentage is {percentage} , So Your Grade is C")
# elif percentage>60 and percentage<=70:
#     print(f"Your Percentage is {percentage} , So Your Grade is D")
# else:
#     print(f"Your Percentage is {percentage} , So Your Grade is F")

# # Pass or Fail 

# if percentage>60 and  percentage<=100:
#     print(f"You are Pass and your Percentage is {percentage}")
# else:
#     print(f"You are Fail and your Percentage is {percentage}")

# #  subject level checking 

# if eng_marks <= 33 :
#     print(f"You are Fail in English . your obtained marks in english are {eng_marks}")
# if maths_marks <= 33:
#     print(f"You are Fail in Maths . your obtained marks in maths are {maths_marks}")
# if phy_marks <=33 :
#     print(f"You are Fail in Physics . your obtained marks in physics are {phy_marks}")
# if chem_marks <=33:
#     print(f"You are Fail in Chemistry . your obtained marks in chemistry are {chem_marks}")
# if bio_marks <= 33:
#     print(f"You are Fail in Biology . your obtained marks in Biology are {bio_marks}")

# # Scholarship Eligibility check 

# if percentage>=90 :
#     print("You are Eligible for Scholarship . Congratulations!")
# else:
#     print("You are not Eligible for Scholarship.")

# +++++++++++++++++
#   LOOPS 
# +++++++++++++++++

#  Without While Loop 

# print("Hello WOrdl")
# print("Hello WOrdl")
# print("Hello WOrdl")
# print("Hello WOrdl")
# print("Hello WOrdl")
# print("Hello WOrdl")
# While loop -- eliminate the need of creating multiple copies of the same thing like above , it represent 
# the repeatable block of code untill the condition become false 
# With While Loop 
# Will print Hello world 5 times with while loop untill the condition i<=5 become false.
# i = 1
# while i<=5:
#     print("Hello World")
#     i+=1

# Exampele with Grading system 
# eng_marks = int(input("Enter your English Marks: "))
# maths_marks = int(input("Enter your Maths Marks: "))
# urdu_marks = int(input("Enter your Urdu Marks: "))
# phy_marks = int(input("Enter your Physics Marks: "))

 
# marks_list = [eng_marks, maths_marks, urdu_marks,phy_marks]

# subject_name = ["English","Maths","Urdu","Physics"]
# i = 0 
# while i < len(marks_list):
#    if marks_list[i]<=33:
#       print(f"Fail in {subject_name[i]}")
#    i+=1

# example 2
# counting 
# num = 1 
# while num<=10:
#     print(num)
#     num+=1

# example 3
#sum
# num = 1
# total = 0

# while num<=5:
#     total = total+num 
#     num+=1
# print("Sum is : " , total)

#exampel 4
# Multiplication table of a number
# n = int(input("Enter a number : "))
# i = 1
# while i<=10:
#     print(f"{n} x {i} = {n*i}")
#     i+=1

# example 5
# Reverse countin 
# n= 10 
# while n>=1:
#     print(n)
#     n-=1
# print("Blast off")

# example 6
# keep asking untill correct password
# password=""
# while password != "1234":
#     password = input("Enter Password: ")
# print("Access Granted!")

# example 7
# sum numbers untill user types 0

# total = 0
# number = int(input("Enter a number(0 to stop): "))

# while number != 0:
#     total = total+number 
#     number = int(input("Enter a number (0 to stop): "))
# print("Total sum is : " , total)

# exmaple 8 
# num = 1
# while num <=10 :
#     if num % 2 == 0 :
#         print(f"{num} is Even")
#     else:
#         print(f"{num} is Odd")
#     num = num+1

# exmaple 9 
# simple menu 
# while True:
#     print("1. Say Hello")
#     print("2. Exit")
#     choice= input("Enter Choice: ")
#     if choice== "1":
#         print("Hello")
#     elif choice == "2":
#         print("GoodBye!")
#         break
#     else:
#         print("Invalid Choice , try again")


#Task 6 ++++++++++++++++++ Leap Year 
# Leap year 
# year = 1900
# leap_years = []
# while year <= 2026:
#     if year% 4 ==0 and year%100==0:
#         if year% 400 ==0:
#             print(f"{year} is a leap year")
#             leap_years.append(year)
#         else:
#             print(f"{year} is not a leap year.")
    
#     elif year % 4 == 0 and year%100 !=0:
#         print(f"{year} is a Leap Year")
#         leap_years.append(year)

#     else:
#         print(f"{year} is not a leap year.")
#     year+=1
# print(leap_years)
# Task -- bonus can be decide on the salary base too.

#Task 7++++++++++++++++++++ employee salary system 

# Employee Salary System (with Bonus , Tax )
# while True:
#     emp_name = input("Enter your Name: ")
#     emp_salary = int(input("Enter your Salary: "))
#     experience_in_years = int(input("Enter your Experience: "))
# #Bonus Calculation using If-elif-else
#     if experience_in_years>=10:
#         bonus = emp_salary*0.20
#         total_salary = emp_salary+bonus
#         print(f"with experienceof 10+ years the salary with 10% bonus is {total_salary} ")
#     elif experience_in_years >5 and experience_in_years<10:
#         bonus = emp_salary*0.10
#         total_salary = emp_salary+bonus
#         print(f"with experienceof 5+ years the salary with 10% bonus is {total_salary}")
#     else:
#         bonus = emp_salary*0.05
#         total_salary = emp_salary+bonus
#         print(f"with  no experience the salary with 5% bonus is {total_salary}")

# # Tax Calculation 
#     if emp_salary>100000:
#         tax = emp_salary* 10/100
#         total_salary_0=emp_salary-tax
#         print(f"Above this 100000 Salary the Tax that will be implmented will be {tax}")
#     elif  emp_salary>50000:
#         tax = emp_salary* 5/100
#         total_salary_0 = emp_salary-tax 
#         print(f"with  this Range of 50000-100000 Salary the Tax that will be implemented will be {tax} ")
#     else:
#         tax = emp_salary*2/100
#         total_salary_0 = emp_salary-tax 
#         print(f"with Basic Salary the tax that will be implmented will be {tax} ")


#     net_salary = emp_salary+bonus-tax
#     print(f"After Adding Bonus {bonus} deducting Tax {tax} the Net Salary is {net_salary}")
#     choice = input("Do you want to calculate the Salary of another employee: (yes,no)  ")
#     if choice == "no":
#         break
#++++++++++++
# While loop Practice
#++++++++++++

#Infinite loop 
# while True:
#     print("Hello World")

# This is called an Infinite Loop 

# Practice
#print number from 1 to 100
# i = 1
# while i<=100:
#     print(i)
#     i+=1

#print number from 100 to 1

# i = 100 
# while i>=1:
#     print(i)
#     i-=1
# Traverse a list 
# nums =  [1,2,3,4,14,17,23,28,81]
# i = 0 
# while i < len(nums):
#     print(nums[i])
#     print(nums)
#     i+=1

# Search an element in list 

# nums = [1,4,9,34,45,88,67,44]
# x =44
# i=0
# while i <len(nums):
#     if(nums[i]==x):
#         print("Found at index" , i)
#     i+=1

# Break Statement 
# Break immediately stops the loop 

# i = 1
# while i<=10:
#     if(i==4):
#         break
#     print(i)
#     i+=1

# Break example for searching 
# nums = [1,2,3,4,5,6,7,8]

# x = 5
# i = 0
# while i < len(nums):
#     if(nums[i]==x):
#         print("Found")
#         break
#     i+=1
    
# Continue Statement 

#continue statement skips the current iteration
#and move to the next one 
#example 

# i = 1
# while i<=10:
#     if (i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

#++++++++++++++++++++++++++++++++++++
# For Loop
#________________________
# Definition: 
#A for loop lets you go through each item in a collection, one at a time, automatically — running the same block of code once for every item, without you manually writing a repeat condition like you do with while
#syntax 
# for item in collection:
# for is loop 
# item : a variable name you choose — it holds one element at a time, automatically updated each pass
# collection : anything you can loop over (list, tuple, string, dictionary, set, file, etc.)
# No manual counter, no manual condition, no manual increment — Python does all of that internally

# simple example :
fruits = ['apple' , 'banana' , 'cherry']
for fruit in fruits:
    print(fruit)

# Using For loop with different  data types 
# with list 
number = [10,20,30,40,50]
for num in number:
    print(num)
#with tuple
coordinates = (4,5,6)
for i in coordinates:
    print(i)
#with a string 
name = "Aiman"
for char in name:
    print(char)
# with a dictionary 

student = {"name" : "Aiman" , "age" : "22"}
for key in student:
    print(key)
for key , value in student.items():
    print(key, ":" , value)

# with set 

unique_numbers = {1,2,3,2,1}
for num in unique_numbers:
    print(num)

# common methods / functions  paired with for lopps 

# range() -- generates a sequence of numbers to loop through, useful when you want to repeat something a specific number of times without looping over an actual collection:
# range(start, stop, step) → this is a separate function that generates numbers, which you then loop over using the for syntax above.
for i in range(5):
    print(i)

# enumerate() — gives you both the index and the item at once, useful when you need to know the position too:

fruits = ['apple', 'banana' , 'cherry']
for index , fruit in enumerate(fruits):
    print(index,fruit)

#++++++++++++++++++++++++
# For Loop Practice 
# 1st Practice  
# Print numbers from 1 to 10 using range() -- 
for i in range(1,11):
    print(i)

# 2nd Practice
# Print each character of your name — loop through a string.
name = "Aiman"
for char in name:
    print(char)

# 3rd practice
# Sum all numbers in a list
list_0 = [4,8,12,16,20,24,28,32,36,40]
total =0
for l in list_0:
    total += l
print(total)

# 4th Practice 
# Print only even numbers from a list
list_1 = [2,3,6,9,11,24,33,44]
for num in list_1:
    if num%2==0:
        print(num)
    else:
        continue
# 5th Practice 





















#++++++++++++++++++
#Function -- is a block of code 
#that perform a specific task .
#It helps us avoid writing the same code again and again .
#+++++++++++++

#function syntax

# def funcion_name (parameters):
#     Code
#     return value 
# # function call 
# function_name(arguments)

#example

# def hello():  #function declaration 
#     print("Hello Everyone") #code
# #function calling by its name
# hello()
# #if i wanna print hello evveryone 5 times i just simply call that function 5 times 

# hello()
# hello()
# hello()
# hello()
# hello()

# def greetings():
#     print("Hey Nice to meet you!")
# greetings()

# # Function with Parameters 
# # parameters : are variables , written while creating a function , they can be 2,3,4,5,100..

# #example

# def add(a,b,c):  # Function declaration with parameters 
#     sum=a+b+c    # save the values of a ,b and c in sum variable
#     print(sum)
# # call the function with the values or can say arguments of the varaible declare in the creation of function -- 5 is the value of a , 10 --b , 15--c.
# add(5,10,15)
# #arugments -- are actual values passed while calling .

# # a ,b , c --- parameters
# # 5,10,15 --- Arguments 

# # Example 
# #one way of calling the function with arguments
# def school(name , city , age):
#     print(name)
#     print(city)
#     print(age)

# school("aiman","fsd",22)
# # 2nd way of calling the fucntion with arguments 
# def school(name , city , age):
#     print(name)
#     print(city)
#     print(age)
# fname = "Aiman"
# fcity = "Fsd"
# fage = "22"
# school(fname , fcity,fage)
# # 3rd way of calling the function with arguments 
# def school(name , city , age):
#     print(name)
#     print(city)
#     print(age)
# fname = input("Enter your name : ")
# fcity= input("Enter your city: ")
# fage = input("Enter your age: ")
# school(fname,fcity ,fage)
# # + example
# def sum(x,y):
#     x+=5
#     y+=9
#     z = x+y
#     print(z)
# sum(2,3)


# # Fucntion with Return Value 
# # Return Value -- sends a value back from the function 

# def sum(a,b):
#     z=a+b 
#     return z 

# result = sum(2,10)
# print(sum(2,10))
# print(result)
# # we can call the function by its name calling or the object calling 
# # result here is the object or we can say a variable 


# #++++++++++++++++++++
# # Built-in Functions --python already provide many  built-in functions 
# #+++++++++++++++++++
# #example 
# print("hello")  #display the output 

# len(list) #return the length 

# type(name_0)  # return the datatype 

# range(0)  #Generate Sequence of numbers.

# # example

# name ="saim"
# print(name)
# print(len(name))
# print(type(name))


# #+++++++++++++++++++
# # User Defined Functions -- functions created by the programmer , are called user defined functions
# #+++++++++++++++++++

# #example 

# def greet():
#     print("Welcome")
# greet()


# ########
# # Functions practice 
# #######

# # example 1 
# # simple menu 
# def show_menu():
#     print("1. Add Dishes")
#     print("2. View All")
#     print("3.Exit")
# show_menu()

# # example 2
# # simple calculation with no input 

# def show_pi():
#     pi = 3.14159
#     print(f"The Value of pi is {pi}")
# show_pi()

# # Example 3 
# # Greeet a Specific person 

# def greet(name):
#     print(f"Hello , {name} ! Welcome to Python. ")
# greet("Fatima")
# greet("azka")

# # example 4
# # Add two numbers 
# def add_num(a,v):
#     total = a+v
#     print(f"The sum of {a} and {v} is {total}")
# add_num(3,4)
# add_num(6,7)
# #example 5 
# # chech the function odd or even 

# def check_even_odd(num):
#     if num%2==0:
#         print(f"{num} is Even")
#     else:
#         print(f"{num} is Odd")
# check_even_odd(9)
# check_even_odd(98)
# check_even_odd(79)
# check_even_odd(56)

# # example 6 
# # multiple parameters -- mini version of grading logic define above 

# def calculate_percenatge(obtained, total):
#     percentage = (obtained/total)*100
#     print(f"Percentage: {percentage}%")

# calculate_percenatge(450,500)
# calculate_percenatge(381,500)

#++++++++++++++++++++++++ Key difference to notice
# # Without parameters |	With parameters
# # def greet():       |	def greet(name):
# # Always does the    |
# # exact same thing   |	Behavior changes based on what you pass in
# # Called like       |
# # greet()	        |        Called like greet("Aiman")
# #+++++++++++++++++++++++
# # Return value conceptual understanding 
# def sum(x, y):
#     x += 5
#     y += 9
#     z = x + y
#     print(z)

# result = sum(2, 3)
# print("Now checking result:", result)

#Running the function (always happens when called, regardless of return)
#Displaying something (print() — one-time visual output, not reusable)
#Returning something (return — hands the value back so it can be stored/reused/built upon)


# Task 7++++++++++++++++++++Bill system 

# def bill_estimation(consumed_units):
    
#     if fconsumed_units<=100 :
#         bill = fconsumed_units*10
#         print(f"Your bill with 100 units are {bill}")
#     elif fconsumed_units>=200 or fconsumed_units >=300:
#          bill = (fconsumed_units*10) + ((fconsumed_units-100)*15)
#          print(f"Your bill with units 200 or 300 are {bill}")


#          return bill
# fconsumed_units = int(input("Enter your used units: "))
# net_bill = fconsumed_units
# bill_estimation(fconsumed_units)
# print(net_bill)


#+++++++++++++++++++
# Default parameters
#default parameter have a default value 
#if no argument is given, 
#the default value is used.
# def student(name="aiman"):
#     print(name)
# student()   #use default parameter that is declare in function define 
# student("Ali")  #argument given and its override


#practice 1 : print list elements 
# nums = [1,2,3,4,5,6]
# def numbers(list):
#     for item in list :
#         print(item)
# numbers(nums)

# # practice 2
# #find the length of list

# list_0 = [9,8,7,6,5,4,3,2,1]
# def length(list):
#     print(len(list_0))
# length(list_0)

# #practice 3 
# #USD to INR converter 

# def converter(usd):
#     inr = usd*83
#     print(inr)
# converter(10)




#+++++++++++++++++++
# Recursion -- means a function calling itself again and again . Every Recursive function must have a base case . Base case is the condition of recursive function 
# with base case recursive function become infinite 
#+++++++++++++++++++

# print n to 1

# def numbers(n):
#     if n>5:
#         return
#     print(n)
#     numbers(n+1)
# numbers(1)

# def numbers_0(n):
#     if n>100:
#         print("Number is Greater then 100.")
#         return
#     print(n)
#     numbers_0(n+1)
# fn = int(input("Enter your number: "))
# num = fn 
# numbers_0(fn)

#print a list using recursion

# number = [1,2,3,4,5,6,7,9,10]
# def print_list(list , index):
#     if (index==len(list)):
#         return 
#     print(list[index])
#     print_list(list,index+1)
# print_list(number,0)

# ============================================
# Difference Between Loop & Recursion
# ============================================

# Loop
# Uses for or while.

# Faster.

# Uses less memory.

# Easy for repeated work.


# Recursion
# Function calls itself.

# Easier for tree and divide-and-conquer problems.

# Uses more memory due to function calls.

# ============================================
# Quick Revision
# ============================================

# def
# Used to create a function.

# Function
# Reusable block of code.

# Parameter
# Variable in function definition.

# Argument
# Actual value passed to function.

# return
# Sends value back.

# Built-in Function
# Already provided by Python.

# User Defined Function
# Created by programmer.

# Default Parameter
# Parameter with default value.

# Recursion
# Function calling itself.

# Base Case
# Stops recursion.

# len()
# Returns length.

# range()
# Generates sequence.

# print()
# Displays output.

# type()
# Returns data type.


#+++++++++++ 
# Functions more practice 
#+++++++++++

# Basic Practice Set
# Square a number 

# def number(n):
#     square = n*n
#     return square
# print(number(3))

# Even or Odd checker 

# def even_odd(n):
#     if n%2==0:
#         return(f"{n} is a even number")
#     else :
#         return(f"{n} is not a even numebr")

# print(even_odd(88))
# find the largest number among the 3 numbers 

# def largest_num(x,y,z):
#     if x>y and x>z:
#         return(f"{x} is the largest number")
#     elif y>x and y>z:
#         return(f"{y} is the largest number")
#     else:
#         return(f"{z} is the largest number")
# print(largest_num(77,66,88))

#Convert  celsius to Fahrenheit 

# def temp_converter(celsius):
#     fahrenheit = (celsius*9/5)+32
#     return fahrenheit
# print(temp_converter(99.2))

# # Calculate simple Intereset
# def intereset(principal,rate ,time):
#     simple_intereset = (principal*rate*time)/100
#     return simple_intereset
# print(intereset(1000,5,2))


#______________________
# File Handling in python (File I/O)
# File  I/O means -- input and output operations on files 
#Python allow us to 
# #read data from the file 
# write data into files 
#Types of files 

#1. Text File 
# stor data in readable text format 
# example 
#.txt 
#.docs
#.log
#.csv 
#2. Binary Files 
# store data in binary format 
# example
# .png 
#.jpg
#.jpeg
#.mov
#.pdf

# File operations 
# Openning a file 
# syntax 

# f = open("filename " , "mode")

# methods to access the files through path 
# 1st to aceess the file from the same folder
 
# f = open("./text.txt" , "r")

# 2nd to access the file from the different folder but main folder is the same 

# f = open("./practice/aiman.txt","r")

# 3rd to access the file from the nested folders 

# f = open("./practice/main/smallest.txt" , "r")

# 4th  to access the files from outside the main folder 
# f = open("../outer.filename" , "mode")

# example 
# f = open("./text.txt" , "r")

# File Modes 

# "r"
# Read mode
# Opens existing file.

# "w"
# Write mode
# Creates new file if it doesn't exist.
# Overwrites existing file.

# "a"
# Append mode
# Adds data at the end.
# Creates file if it doesn't exist.

# "x"
# Create mode
# Creates a new file.
# Gives error if file already exists.

# "r+"
# Read and Write.

# "w+"
# Write and Read.

# "a+"
# Append and Read.


# Reading a file 

# example 

# f = open("./text.txt" , "r")
# data =f.read()
# print(data)
# f.close  #closing the file is optional  because it close automaticly 

# Read Specific characters 

# f = open("./text.txt","r")
# data = f.read(3)
# # data = f.tell()
# f.seek(4)
# print(data)
# f.close()

# ReadLine()
# reads one line at a time 

# f = open("text.txt","r")

# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close()

# Closing the file 

# Always close the file after using it .
# f.close()

# Wrting a file 

# write()

# f = open("text.txt" , "r+")
# data = f.read()
# print("old data" , data)
# f.write("\tSoftware House")
# #read updated content
# f.seek(0)  # move the cursor to the start of the file 
# data = f.read()
# print("New Data" , data)
# f.close()

# Append Mode 

# f = open("text.txt" , "a")
# f.write("\n institute")
# f.close()


# With Statement 

# with automatically closes the file .
# No need to call close().

# with open("text.txt" , "r") as f:
#     data =f.read()
#     print(data)
# #file close automatically


# Creating a new file 

# example

# f = open("practice.txt","x")
# f.write("Hello")
# f.close()
#creates file if it does not exist .

# Deleting a file 
#python use os module 
# import os 
# os.remove("./practice/aiman.txt")

# Module
# ============================================

# A Module is a file
# written by another programmer.

# It contains useful functions.

# Example

# import os

# import math

# import random




# Practice set of Files 

# Create and write a file

# f = open("demo.txt","w")
# f.write("Hi everyone\n")
# f.write("We are learning File I/O\n")
# f.write("Using Python\n")
# f.write("I like Programming in python")
# f.close()

# Practice 2 
# Replace Java with Python 

# with open("demo.txt","r") as f:
#     data = f.read()
# new_data = data.replace("Python" , "python")
# new_data = data.replace("Java" , "Python")
# with open("demo.txt","w") as f:
#     f.write(new_data)

# Practice 3
#Search word

# word = "python"

# with open("demo.txt","r") as f:
#     data = f.read()
#     if(word in data):
#         print("Found")
#     else:
#         print("Word Not Found")

# Practice 4
# Find Line Number 

# word = "python"
# line_no =1
# with open("demo.txt" , "r") as f:
    # for line in f:
        # if(word in line):
            # print("Found at line ", line_no)
            # break
        # line_no+=1
    # else:
        # print(-1)
# Practice 5
#count event numbers 
#suppose file contains
# 1,2,3,4,5,6,7,8
# with open("numbers.txt","r") as f:
    # data = f.read()
# nums = data.split(",")
# count = 0
# for num in nums:
    # if(int(num)%2==0):
        # count+=1
# print(count)

# Quick Revision 

# open()
# Opens a file.

# close()
# Closes a file.

# read()
# Reads complete file.

# read(n)
# Reads first n characters.

# readline()
# Reads one line.

# write()
# Writes data.

# append()
# Adds data at end using "a" mode.

# with
# Automatically closes file.

# import
# Imports module.

# os.remove()
# Deletes a file.

# replace()
# Replaces old text with new text.

# split()
# Splits string into list.

# in
# Checks whether a word exists.

# "r"
# Read Mode.

# "w"
# Write Mode.

# "a"
# Append Mode.

# "x"
# Create New File.


# Practice of Files 
#example 1 -- simple read and print 

# f = open("./text.txt" , "r")
# data = f.read()
# print(data)
# f.close()

# # example 2 -- count lines 
# count =0
# f = open("./text.txt" , "r")
# for line in f :
#     count+=1
  
# print(count)

# example 3 -- count the words 

# f = open("./text.txt","r")
# data = f.read()
# words = data.split()
# count_words = 0
# for word in words:
#     count_words+=1
# print(count_words)

# example 4 -- print only non - empty lines 
# with open("./text.txt" ,"r") as f:
#     for line in f:
#         if line.strip() != "":
#             print(line)

# Example 5 -- writing the name or age to the file
# with open("./text.txt" , "w+") as f:
#     username=input("Enter your name: ")
#     age = (input("Enter your age: "))
#     f.write(username)
#     f.write(age)
#     f.seek(0)
#     data = f.read()
#     print(data)
# Example 6 --    append to a file 
# with open("./text.txt" , "a") as f:
#     username=input("Enter your name:\n")
    
#     age = (input("Enter your age:\n "))
#     f.write(username +  "\n" + age)
#     # f.write(username)
#     # f.write(age)

# Example 7-- count vowels
# with open("./text.txt" , "r") as f:
#     vowels = "aeiou"
#     count =0
#     data = f.read()
#     for i in data:
#         if i in vowels:
#             count+=1
            

#     print(count)

# Example 8-- replacing the existing word in file with other words

# with open("./text.txt", "r+") as f:
#     data = f.read()
#     data = data.replace("aiman" ,"fatima")
#     f.seek(0)
#     f.write(data)
#     print(f)


# example 9--  copy the content of one file into another file

# with open("./text.txt","r") as f1 ,  open("demo.txt" , "w") as f2:
#     data = f1.read()
#     f2.write(data)

# example 10-- count how many times a specific word appears

# with open("./demo.txt" , "r") as f:
#     data = f.read()
#     target = "fatima"
#     count = 0
#     words = data.split()
#     for word in words:
#         if word == target:
#             count+=1
# print(count)


#+++++++++++++++++++++
# Functions Simple Examples

# Restaurant Bill Splitter 
# In short: it takes 4 fixed food item prices → adds a weekend service charge → splits the total between however many people you enter → adds a 10% tip per person → prints how much each person owes, rounded to cents
# noodles = 12.50
# coca_cola = 8.75
# white_sauce_pasta = 22.00
# cheese_rolls = 15.25
# items_sum = noodles + coca_cola + white_sauce_pasta + cheese_rolls
# service_charges = 0
# is_weekend= True
# if is_weekend == True:
#     sub_total=items_sum + (items_sum*15/100)
# else:
#     sub_total = items_sum + (items_sum * 10/100)
# def split_bill(num):
#    amount_to_pay_per_person =sub_total/num
#    return amount_to_pay_per_person
# fnum = int(input("Enter how many persons are: "))
# per_person =split_bill(fnum)
# print(per_person)

# def tip_per_person(pay):
#     tip = pay + (pay*10/100)
#     return tip 
# final_amount = tip_per_person(per_person)
# print(final_amount)

# print(f"{final_amount: .2f} amount each person needs to pay")

# Movie Ticket Pricing 


# def ticket_price(age):
#     if age<12:
#         ticket_cost = 5
#     elif age>=60:
#         ticket_cost = 8 
#     else:
#         ticket_cost = 12
#     return ticket_cost

# def total_cost(ages):
#     total = 0 
#     for age in ages:
#         total = total + ticket_price(age)
#     return total
# fages = [8,34,65,17,70]
# cost = total_cost(fages)
# print(cost)


# Simple Grading System 

# def get_grade(marks):
    
#     if marks>=90:
        
#          return"A" 
#     elif marks>=80 and marks<=89:
         
#          return "B"
#     elif marks>=70 and marks<=79:
          
#           return "C"
#     elif marks>=60 and marks<=69:
          
#           return "D"
#     else :
#           return "F"
    
# fmarks=int(input("Enter your marks : "))
# Grade = get_grade(fmarks)
# print(f"{fmarks} your grade is {Grade}")

# Password Strength Checker 

# password = input("Enter a password: ")

# length_ok = False 
# has_number = False 
# has_capital = False

# if len(password) >=8:
#      length_ok = True
# for letter in password:
#      if letter>= "0" and letter <="9":
#           has_number = True 
#      if letter >= "A" and letter <= "Z":
#           has_capital = True
# if length_ok == True and has_number == True and has_capital == True:
#      print("Strong Password!")
# else:
#      print("Weak Password")

#++++++++++++++++++++++++++++
# File Handling More Practical Examples 

# Todo List saver 
#1st adding tasks to the todo list 
# def add_task(task):
#     with open("./todo.txt" , "a") as f:
#         f.write(task + "\n")

# # 2nd reading the content of the file and printing it 
# def show_tasks():
#     with open("./todo.txt" , "r") as f:
#         data = f.read()
#         print(data)

# while True:
#     choice = input("Type 'add' to add a task , 'show' to view tasks , or exit to quit: ")
#     if choice == "add":
#         user_task = input("Enter your tasks: ")
#         add_task(user_task)
#     elif choice =="show":
#         show_tasks()
#     elif choice == "exit":
#         break 
#     else:
#         print("Invalid Choice , try again.")


#Expense Tracker 
# def add_expense(item , amount):
#     with open ("./expense.txt" , "a" ) as f:
#         f.write(item + " - " + amount + "\n")
# def show_expenses():
#     with open("./expense.txt" , "r") as f:
#         data = f.read()
#         print(data)
# def total_expense():
#     total=0
#     with open("./expense.txt" , "r") as f:
#         for line in f:
#             parts = line.split(" - ")
#             amount_text = parts[1].strip()
#             amount_number = int(amount_text)
#             total = total + amount_number
#         return total 

# while True :
#     choice = input("Enter your choice : Type 'add' to log an expense, 'show' to view all expenses, 'total' to see total spent, or 'exit' to quit")
#     if choice == "add":
#         item = input("enter your stuff: ")
#         amount = input("Enter the price : ")
#         if amount.isdigit():
#             add_expense(item, amount)
#         else:
#             print("Invalid amount, please enter numbers only.")
#     elif choice == "show":
#         show_expenses()
#     elif choice == "total":
#         net_total =total_expense()
#         print(f"Your Total is: {net_total}")
#     elif choice=="exit":
#         break
#     else:
#         print("Invalid Choice . Try again")


# Simple Contact Book 

# def add_contact(name , number ):
#     with open("./contacts.txt" , "a") as f:
#         f.write(name + " - "  + number  +  "\n" )

# def show_contacts():
#     with open("./contacts.txt" , "r") as f:
#         data = f.read()
#         print(data)

# def find_contact(search_name):
#     with open("./contacts.txt" , "r") as f:
#         found = False
#         for line in f:
#             parts = line.split(" - ")
#             if len(parts)==2:
#                 contact_name= parts[0].strip()
#                 if search_name == contact_name:
#                     print("Found! Number:" , parts[1].strip())
#                     found= True 
#     if not found:
#         print("Contact not Found")

# def delete_contact(name_to_delete):
#     with open("./contacts.txt" , "r") as f:
#         lines = f.readlines()
#     remaining_contacts = []
#     found = False
#     for line in lines :
#         parts = line.split(" - ")
#         if len(parts)==2:
#             contact_name = parts[0].strip()
#             if contact_name== name_to_delete:
#                 found= True
#             else:
#                 remaining_contacts.append(line)
#     with open("./contacts.txt" , "w") as f:
#         f.writelines(remaining_contacts)
#     if found:
#         print("Contact Delete Successfully")
#     else:
#         print("Contact not Found.")

# while True:
#     choice = input("Enter your choice Type Add to add a Contact , show to view all contacts , find to search a contact , delete to remove a contact ,  exit to quit: ")
#     if choice == "Add":
#         name = input("Enter your name: ")
#         contact = input("Enter your contact: ")
#         add_contact(name , contact)
#     elif choice == "show":
#         show_contacts()
#     elif choice == "find":
#         search_name= input("Enter your name to search the contact: ")
#         find_contact(search_name)
#     elif choice == "delete":
#         name_to_delete = input("Enter the name to delete: ")
#         delete_contact(name_to_delete)
#     elif choice=="exit":
#         break
#     else :
#         print("Enter a valid choice.Try Again.")

#+++++++++++++++++++++++++++++++++
# OOP - Object Oriented Programming

# OOP (Object-Oriented Programming) is a programming paradigm
# that organizes code into Classes and Objects.
#
# Real-Life Example:
# Think about a School.
# - Student = Object
# - School Blueprint = Class

# 1. CLASS

# Definition : 
# A Class is a blueprint (template) used to create objects.

# Real-Life Example:
# A house map is a blueprint.
# Many houses can be built using the same blueprint.

# class Class:
#     # Class Variable 
#     brand = "Toyota"
#     color = "White"
# # Accessing the class variables  using class name
# obj = Class()
# print(obj.brand)
# print(obj.color)

# 2. OBJECT 

# Definition :
# An Object is an instance of a class.

# Real-Life Example:
# Car = Blueprint
# Toyota, Corolla = Object

# class student:
#     name = "Ahsan"
#     name="ali"
# # Creating Objects 
# obj= student()
# obj_1 = student()
# # accessing the object data 

# print(obj.name)
# print(obj_1.name)   # it print name 2 times due to overwriting of name variable


# 3. Constructor 
# Definition :
# Constructor runs automatically whenever an object is created
# It is mainly used to intialize object data 

# class student :
#     # Constructor 
#     def __init__(self, name , age):
#         #Instance Variables
#         self.name1 = name 
#         self.age1 = age 
# #Creating object 
# obj = student("ALi", 22)
# print(obj.name1)
# print(obj.age1)

# 4 . Self Keyword 

#Definition :
# Self refers to the current object.
# It allows us to access object variables and methods
# Real Life Example 
# "My Name is Ali."
# Here "My" means the current person.

# class demo:
#     def set_name(self , name):
#         # store value in current object 
#         self.name1 = name
#     def show(self):
#         pass
#     def d(self):
#         print("Student Name: ", self.name1)
# obj = demo()
# obj.set_name("Ahsan")
# obj.d()

#5 . Instance Variables 
# Definition:
# Variables created using self are called Instance Variables.
# Every object has its own copy.

# class student:
#     def __init__(self,name):
#         self.name = name 

# obj1= student("Ali")
# obj2= student("Ahmed")
# print(obj1.name)
# print(obj2.name)


#6. Methods 
# Definition :
# Methods are Functions written inside a class 

# Real _life Example :

# Calculator methods 
# Add
# Subtract 
# Multiply 

# class student():
#     def greet(self):
#         print("Welcome to Python OOP")
# obj = student()
# obj.greet()



#++++ Class , Objects , Self examples 
# Practice 1:
# class book:
    # def __init__(self , title , author , pages):
        # self.title = title
        # self.author = author 
        # self.pages = pages 


    # def show_details(self):
        # print(f'"{self.title}" by {self.author} , {self.pages} pages')

# book1 = book("Harry Potter" , "J.K. Rowling" , 500)
# book2 = book("Mr Chips" , "WIlliam " , 799)
# book1.show_details()
# book2.show_details()
# Practice 2:
# class BankAccount:
#     def __init__(self , owner_name , balance):
#         self.owner_name = owner_name
#         self.balance = balance

#     def deposit(self,amount):
        
#         self.balance = amount+self.balance
#     def withdraw(self , amount):
         
#         if amount> self.balance:
#             print("Insufficinet Balance")
#         else :
#             self.balance = self.balance-amount
#     def show_balance(self):
#         print(f"{self.balance} is your current balance")

# id_1 = BankAccount("Ali" , 34000)
# id_1.show_balance()
# id_1.deposit(1000)
# id_1.show_balance()
# id_1.withdraw(500)
# id_1.show_balance()


# # Employee class 

# class Employee():
#     def __init__(self,name,salary):
#         self.emp_name = name
#         self.emp_salary = salary

# emp_1 = Employee("Aiman" , 30000)
# print(emp_1.emp_name  )   
# print(emp_1.emp_salary)   
# emp_2 = Employee("Faiqa" , 30000)
# print(emp_2.emp_salary)
# print(emp_2.emp_name)























# Task Clacualtor using class and objects 

# class Calculator:

#     def sum (self,x,y):
#         sum = x+y
#         return sum 
#     def subtract(self ,x,y):
#         subtract = x-y
#         return subtract 
#     def multiply(self , x,y):
#         multiply = x*y
#         return multiply
#     def divide (self,x,y):
#         divide = x/y
#         return divide
# obj = Calculator()
# while True :
#     choice = input ("Enter your operation : enter sum for add , subtract for minus , multiply for multiplication , divide for division , exit for quit ")
#     if choice=="exit":
#                 print("")
#                 break 
#     x = int(input("Enter the 1st number: "))
#     y = int(input("Enter the  2nd number: "))
    
#     if choice == "sum" :
#         result =obj.sum(x,y)
#         print(result)
#     elif choice == "subtract":
#         result = obj.subtract(x,y)
#         print(result)
#     elif choice == "multiply":
#         result = obj.multiply(x,y)
#         print(result)
#     elif choice == "divide":
#         result = obj.divide(x,y)
#         print(result)

#     else :
#         print("Invalid choice")




    