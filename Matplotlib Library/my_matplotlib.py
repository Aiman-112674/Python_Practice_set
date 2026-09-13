# Matplotlib:
#  What it is

# Matplotlib is a Python library that turns your data (numbers, lists, DataFrame columns) into visual charts — lines, bars, dots, shapes — anything that helps you SEE patterns instead of just reading numbers.

# Why we need it (the real reason, not just "it's useful")

# Humans are naturally much faster at spotting patterns VISUALLY than by reading raw numbers. Consider:

# Sales: 100, 105, 98, 250, 102, 99, 103

# Reading this list, you might glance right past the 250 sitting in there. But if you PLOT it as a line graph, that 250 visibly JUMPS UP like a spike — your eye catches it instantly, without even trying.


#Matplotlib usually comes right after cleaning, and before modeling — it's how you truly UNDERSTAND your data before trusting it to a model.

import matplotlib.pyplot as plt
fig , ax = plt.subplots()

# fig → the overall "canvas" — controls things like overall size, saving the whole image, etc.
# ax → the specific plot area — this is where you actually draw your data, set titles, labels, etc.

# Why do we need BOTH, when it seems like just one thing?

# Because a Figure can contain MULTIPLE Axes (multiple mini-plots) side by side!

fig, ax = plt.subplots(1, 2)   # 1 row, 2 columns of plots — TWO axes inside ONE figure

# This creates ONE overall picture (fig), but with 2 SEPARATE plot areas inside it (ax[0] and ax[1]) — like having 2 photos in one frame.


# One-sentence summary

# The Figure is the overall canvas/sheet of paper — it exists mainly to hold one OR MORE Axes together as a single unit, and to control whole-picture things like overall size and saving to a file. The Axes is where your actual graph/data lives.


# # simple example

# fig , ax = plt.subplots()   ## Step 1: create the frame (fig) and the plot area (ax)
# marks = [80,90,70,85,95]    
# ax.plot(marks)           # Step 2: draw data ONTO that plot area
# ax.set_title("Student Marks")    # Step 3: label things — all through 'ax'
# ax.set_xlabel("Student Number")
# ax.set_ylabel("Marks")

# plt.show()     # Step 4: actually display the whole figure

# # ex 
# fig , ax = plt.subplots(figsize=(10,8))
# ax.plot([1,2,3],[4,5,6], label = "Trend")
# ax.set_title("My First Explicit Plot")
# ax.set_xlabel("X Axis")
# ax.set_ylabel("Y Axis")
# ax.set_facecolor("Red")
# ax.legend()

# fig.suptitle("Overall Figure Title", fontsize = 14 ,color = "Black")
# fig.set_facecolor('Orange')
# fig.savefig("my_chart.png",facecolor=fig.get_facecolor())

# Line Plot :
#What it is

# A line plot connects data points with a straight line, in order — showing how a value CHANGES across a sequence (like over time, or over steps).

# Why / When to use it

# Use a line plot when your data has a natural ORDER and you want to see the TREND — is it going up, down, staying flat, fluctuating?

# Good use cases:

# Marks over multiple exams (exam 1, exam 2, exam 3...)
# Temperature over days
# Stock prices over time
# Attendance percentage over months

# # Bad use case: comparing unrelated categories (like "marks of Ali vs marks of Sara vs marks of Zain") — there's no natural ORDER between different people, so a line connecting them would be misleading. That's a job for a BAR chart instead (coming next topic).

exam_number = [1,2,3,4,5]
marks =[65,70,68,80,85]

# fig,ax = plt.subplots()
# # Add markers (dots) at each actual data point:
# ax.plot(exam_number,marks,marker="*" , color="red",linestyle="--")
# ax.set_title("Marks over 5 Exams")
# ax.set_xlabel("Exam Number")
# ax.set_ylabel("Marks")

# plt.show()

# math_marks = [65,70,68,80,85]
# physics_marks =[60,65,72,75,78]

# fig,ax = plt.subplots()
# ax.plot(exam_number,math_marks,label="Math",color="red",marker="D")
# ax.plot(exam_number,physics_marks,label="Physics",color="blue",marker="p")

# ax.set_title("Marks Comparsion")
# ax.set_xlabel("Exam Number")
# ax.set_ylabel("Marks")
# ax.legend()

# plt.show()

# Bar Chart
# What it is

# A bar chart uses rectangular bars to show and compare values across different categories — each bar's HEIGHT represents its value.

# Why / When to use it

# Use a bar chart when you're comparing separate, unrelated categories — things that don't have a natural order/sequence between them (unlike a line chart, which needs order).
#Good use cases:

# Marks of DIFFERENT students (Ali vs Sara vs Zain — no natural "order" between people)
# Number of students per city
# Average marks per subject
# Sales per product

#Bad use case: something naturally ordered/continuous, like marks over TIME — that's better as a line chart, since a line shows the TREND, while bars just show individual comparisons without emphasizing "flow."

import matplotlib.pyplot as plt 
# students = ["ALi","Sara","Zain","Nisa"]
# marks =[60,70,44,77]

# fig , ax = plt.subplots()
# # extra visuals
# # ax.bar(students,marks,color="green")
# # ax.bar(students,marks,color=["red","blue","yellow","black"])
# # Horizontal bars instead of vertical (useful when category names are long):
# ax.barh(students,marks,color="green")
# ax.set_title("Marks by Students")
# ax.set_xlabel("Student")
# ax.set_ylabel("Marks")

# plt.show()

#Comparing TWO groups side-by-side (grouped bar chart)
#This is a common real need — like comparing Math vs Physics marks for the SAME students:

# import numpy as np


# students = ["Ali", "Sara", "Zain", "Nida"]
# math_marks = [80, 90, 70, 85]
# physics_marks = [75, 85, 65, 90]

# x = np.arange(len(students))   # gives you [0, 1, 2, 3] - a position for each student
# width = 0.35    # width of each bar

# fig , ax =plt.subplots()
# ax.bar(x - width/2 , math_marks,width,label="Math")
# ax.bar(x + width/2 , physics_marks,width , label="Physics")

# ax.set_xticks(x)
# ax.set_xticklabels(students)

# ax.set_title("Math vs Physics Marks")
# ax.set_xlabel("Student")
# ax.set_ylabel("Marks")
# ax.legend()

# plt.show()

# Histogram — 

# The first thing to understand is:

# A histogram is used to understand how numerical data is distributed.

# For example, imagine you have the ages of 20 students:

# ages = [12, 13, 12, 15, 14, 13, 16, 12, 14, 15,
#         13, 17, 16, 14, 15, 13, 12, 14, 16, 15]

# You might want to know:

# Are most students around age 12–14?
# Are there many students around 16–17?
# Is the data spread out?
# Where is the data concentrated?

# A histogram is excellent for answering these questions.

#A histogram groups numbers into ranges and counts how many numbers fall into each range.

#Bin

# A bin is simply a range/group of values.

# For example:

# 0–10
# 10–20
# 20–30
# 30–40

# Each one is a bin.

# The histogram counts how many values belong to each bin.

#Easy rule:
# use case 
# Bar plot → categories
# Histogram → distribution of numerical data


# ages = [12, 13, 12, 15, 14, 13, 16, 12, 14, 15,13, 17, 16, 14, 15, 13, 12, 14, 16, 15,17,16,17]

# fig , ax = plt.subplots()
# # plt.hist(ages)
# ax.hist(ages,bins=5,color = "skyblue",edgecolor="black")
# ax.set_xlabel("Age")
# ax.set_ylabel("Number of Students")
# ax.set_title("Distribution of Studnet Age")
# plt.show()

marks = [45, 55, 60, 62, 65, 67, 70, 72, 72, 75,78, 80, 81, 82, 85, 88, 90, 92, 95, 98]
fig , ax = plt.subplots()
# plt.hist(ages)
ax.hist(marks,bins=5,color = "orange",edgecolor="yellow")
ax.set_xlabel("Marks")
ax.set_ylabel("Number of Students")
ax.set_title("Distribution of Studnet Marks")
plt.show()

# Think of it like this:
# Raw data
#    ↓
# 45, 55, 60, 62, 65, 67, ...
#    ↓
# Group into ranges
#    ↓
# Count how many values are in each range
#    ↓
# Draw histogram