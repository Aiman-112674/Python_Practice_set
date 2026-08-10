# print("Hello World")


# name="Aiman" ;
# name1 = "Software Engineer"
# print(name , name1)

# age = 30
# marks = 40.0 
# class1 = "BSSE"

# print(class1)

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

# #Assignment operator  (x+=y,-=,/=,*=,**=,%=,=)
# x = 5
# y = 18 
# x-=y
# print(x)

# #Logical Operator 

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



# Calculator 


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
  
# Strings & its  Functions 

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

name = "we are muslims"
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
self = "aiman zafar "
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
name_0 = "      sania zafar      "
self_0 = "      aiman zafar Iqbal     "
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


# ATM Machine 

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
 

# # Even - odd checker 

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

list = ['ali' , 'raza' , 89 , 76.8 , 33 , 33.2]

# Positive slicing 

# print(list[0:5])
# print(list[1:])
# print(list[0:])

# [0:5] -- it startt from 0 and end at 5 but does not include the 5 in printing , it just print 0-4

# Negative Slicing 


list = ['ali' , 'raza' , 89 , 76.8 , 33 , 33.2]

# print(list[-3:-1])
# print(list[-4:-1])
# print(list[-5:-1])
# print(list[-6:-1])
# print(list[-6:])
# print(list[:-1])


# [-3:-1]  -- -3 this is the ending index and its include means the value at this index is included and -1 is the starting index and its value is not included 

# List Methods 

list_1 = [4,3,2,1,6,7,8]

#append() -- for adding a new value at the end of list 

# list_1.append(7)
# print(list_1)

# list_1.append(10)
# print(list_1)

# list_1.append('Aiman')
# print(list_1)

# sort() 
# sort list in ascending order by default
list_2 = [5,2,1,8,9,10]
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


# Grading Task 

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


#=========
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

#======
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
student = {
    "name" : "Aiman" , 
    "Age" : 22 , 
    "city" : "Faisalabad"
}


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


#Task 
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

# # employee salary system 

# # Employee Salary System (with Bonus , Tax )
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

