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


# Scatter Plot : A scatter plot is used to see the relationship between two numerical variables.
#For example, suppose we have some students:

# Hours studied	Exam marks
# 1	40
# 2	50
# 3	60
# 4	70
# 5	80

# We might ask:

# Does studying more hours relate to getting higher marks?

# A scatter plot lets us see this visually.

# Each student becomes one dot.
# You can see that as hours studied increase, marks also increase.
# that's the basic idea of a scatter plot.

#Think of a dot as (x, y)

# This is important.
# Every dot has two values:
# (x, y)
# For example:
# (1, 40)
# means:
# x = 1 hour studied
# y = 40 marks
# Another student:
# (4, 70)
# means:
# x = 4 hours studied
# y = 70 marks
# So a scatter plot is basically:
# Put many (x, y) points on a graph and look at their relationship.

hours = [1,2,3,4,5]
marks = [40,50,60,70,80]

fig , ax = plt.subplots()

ax.scatter(hours , marks)

ax.set_xlabel("Hour Studied")
ax.set_ylabel("Marks")
ax.set_title("Study Hours vs Marks")

plt.show()

# Why is Scatter Plot useful?

# This is the main reason you'll use scatter plots in Machine Learning.

# You often have two numerical features and want to ask:

# Are these two variables related?

# Height vs Weight : 

height = [150,155,160,165,170,175]
weight = [50,53,57,61,65,70]

fig ,ax = plt.subplots()
ax.scatter(height,weight,color = "orange",s=100)
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
ax.set_title("Height vs Weight")

plt.show()
# You can visually inspect whether taller people tend to weigh more.
# Remember:

# Histogram → distribution of one variable

# Scatter → relationship between two variables


#Pie Chart?

# A Pie Chart is used to show how a whole is divided into different parts.
# Think of a pizza 🍕:
# The whole pizza = 100%
# Each slice = one part of that 100%
# For example, imagine a student's daily time:
# Activity	Hours
# Study	5
# Sleep	8
# Exercise	2
# Other	9
# The total is 24 hours.
# A pie chart shows what portion of those 24 hours belongs to each activity.

activities = ["Study","Sleep","Exercise","Other"]
hours = [9,2,8,5]

fig , ax = plt.subplots()
ax.pie(hours,labels=activities,autopct="%1.1f")

ax.set_title("Daily Time Distribution")

plt.show()

#One important thing

# A pie chart is best when you're showing parts of one whole.
# Good example:
# How a company's budget is divided.
# Not so good:
# Comparing the salaries of 10 employees.
# For comparisons like that, a Bar Plot is usually better.
# What does autopct mean?
# autopct = automatic percentage , "%1.1f%%" tells Matplotlib:1 → show at least one digit,.1f → show 1 decimal place,%% → display the % symbol

#Box Plot?

# A Box Plot is used to understand the distribution and spread of numerical data.

# It is especially useful for finding:

# Median → the middle value
# Spread → how much the data varies
# Outliers → unusual values

# For example, suppose we have students' marks:

# marks = [45, 50, 52, 55, 60, 62, 65, 68, 70, 95]

# Most marks are around 45–70, but 95 is quite far away. A box plot can help us spot that unusual value.

marks = [45,50,52,55,60,62,65,68,70,98]
fig , ax = plt.subplots()
ax.boxplot(marks,patch_artist=True,vert=False)
ax.set_ylabel("Marks")
ax.set_title("Distribution of Student Marks")

plt.show()
# This creates the box plot from our numerical data.
#  What does the box mean?

# Very roughly:

#       |
#       |    ← upper range
#    ┌─────┐
#    │     │
#    │ ─── │  ← median
#    │     │
#    └─────┘
#       |
#       |
#       •    ← possible outlier

# The box represents the middle portion of the data.

# The line inside the box represents the median.
# The individual point far away can represent an outlier.
#patch_artist=True
# It allows the box itself to be filled instead of just being an outline.
#vert=False → makes the box plot horizontal.


# Heatmap--
# A Heatmap is a visualization where colors represent values.
# Imagine you have a table:
#         Math  English  Science
# Math     1.0    0.7      0.8
# English  0.7    1.0      0.6
# Science  0.8    0.6      1.0
# Looking at the numbers is okay, but it's much easier to understand the relationships when we represent them with colors.
# For example:
#         Math   English  Science
# Math     🔴      🟠       🟠
# English  🟠      🔴       🟡
# Science  🟠      🟡       🔴
# That's the basic idea of a heatmap.
# Why is it useful in ML?
# One of the most common uses is viewing a correlation matrix.
# For example, imagine a dataset with:
# Age
# Salary
# Experience
# Education
# We can calculate how strongly these variables are related and then visualize those correlations with a heatmap.
# This helps us quickly see things like:
# "Salary and Experience seem strongly related."

import numpy as np 
data = np.array([
    [1.0,0.7,0.8],
    [0.7,1.0,0.6],
    [0.8,0.6,1.0]
])

fig , ax = plt.subplots()
ax.imshow(data)
ax.set_title("Correlation Heatmap")

plt.show()

# ex
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

fig, ax = plt.subplots()

ax.imshow(data)

ax.set_title("Simple Heatmap")

plt.show()

# example
marks = np.array([
    [80, 75, 90],
    [60, 70, 65],
    [90, 85, 95],
    [50, 55, 60]
])

fig, ax = plt.subplots()

ax.imshow(marks)

ax.set_title("Student Marks Heatmap")
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["Math", "English", "Science"])

ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(["Student 1", "Student 2", "Student 3", "Student 4"])

plt.show()


# 📊 Your 7 Matplotlib Plots — When to Use Which?
# Plot	Where to use	When to use	What it shows	Importance for ML	Basic OO syntax
# 1. Line Plot	Time/ordered data	When values change over time/order	Trend / change	⭐⭐⭐⭐	ax.plot(x, y)
# 2. Bar Plot	Categories	When comparing different categories	Comparison	⭐⭐⭐⭐	ax.bar(x, y)
# 3. Histogram	One numerical variable	When you want to understand its distribution	Distribution / frequency	⭐⭐⭐⭐⭐	ax.hist(data)
# 4. Scatter Plot	Two numerical variables	When checking relationship between variables	Relationship / correlation	⭐⭐⭐⭐⭐	ax.scatter(x, y)
# 5. Pie Chart	Categories that form one whole	When showing proportions/percentages	Part of a whole	⭐⭐	ax.pie(values)
# 6. Box Plot	Numerical data	When checking spread and outliers	Median / spread / outliers	⭐⭐⭐⭐⭐	ax.boxplot(data)
# 7. Heatmap	Matrix/table of values	When you want patterns through colors	Value intensity / relationships	⭐⭐⭐⭐⭐	ax.imshow(data)

# The easiest way to choose

# When you have data, ask yourself:

# 1️⃣ "I want to see a trend."

# Use Line Plot.

# Example:

# Month → Sales
# Jan → 100
# Feb → 120
# Mar → 150
# Apr → 140

# ➡️ ax.plot()

# 2️⃣ "I want to compare categories."

# Use Bar Plot.

# Example:

# Pakistan → 80
# India    → 90
# China    → 100

# ➡️ ax.bar()

# 3️⃣ "I want to see how my numerical data is distributed."

# Use Histogram.

# Example:

# Student marks:
# 45, 50, 52, 60, 62, 65, 70, 72, 90...

# ➡️ ax.hist()

# 4️⃣ "I want to know whether two variables are related."

# Use Scatter Plot.

# Example:

# Hours studied → Marks
# 1 → 40
# 2 → 50
# 3 → 60
# 4 → 70

# ➡️ ax.scatter()

# This is extremely important for ML.

# 5️⃣ "I want to show percentages of a whole."

# Use Pie Chart.

# Example:

# Food     → 40%
# Rent     → 30%
# Transport → 20%
# Other    → 10%

# ➡️ ax.pie()

# Useful, but not a major ML plot.

# 6️⃣ "I want to find outliers and understand spread."

# Use Box Plot.

# Example:

# Salary:
# 30k, 35k, 40k, 42k, 45k, 48k, 200k

# ➡️ ax.boxplot()

# The 200k might stand out as an outlier.

# Very useful in ML during data exploration and cleaning.

# 7️⃣ "I have a table/matrix and want to see patterns using colors."

# Use Heatmap.

# Example:

#           Age  Salary  Experience
# Age        1     .7       .6
# Salary    .7      1       .9
# Experience .6    .9        1

# ➡️ ax.imshow()

# Very useful for correlation matrices.

# 🏆 Which ones are most important for ML?

# I'd rank them like this:

# 🥇 Tier 1 — VERY IMPORTANT

# 1. Scatter Plot ⭐⭐⭐⭐⭐
# Relationships between features.

# 2. Histogram ⭐⭐⭐⭐⭐
# Understand distributions.

# 3. Box Plot ⭐⭐⭐⭐⭐
# Find outliers and understand spread.

# 4. Heatmap ⭐⭐⭐⭐⭐
# Correlation between features.

# 🥈 Tier 2 — IMPORTANT

# 5. Line Plot ⭐⭐⭐⭐
# Especially important for time-series data.

# 6. Bar Plot ⭐⭐⭐⭐
# Useful for categorical comparisons.

# 🥉 Tier 3 — LESS IMPORTANT FOR ML

# 7. Pie Chart ⭐⭐

# Good for presentations and simple proportions, but you'll use it much less in ML.

# 🎨 How to design them?

# Don't try to memorize 50 styling parameters for every plot.

# For now, remember these common things:

# fig, ax = plt.subplots()

# # your plot
# ax.scatter(x, y)

# ax.set_title("My Plot")
# ax.set_xlabel("X Label")
# ax.set_ylabel("Y Label")

# plt.show()

# Then add customization when needed:

# color
# alpha
# s
# marker
# edgecolor
# linewidth

# The design should make the data easier to understand, not just make the chart colorful.

# 🧠 Your ultimate cheat sheet
# TREND?             → Line Plot
# COMPARISON?        → Bar Plot
# DISTRIBUTION?      → Histogram
# RELATIONSHIP?      → Scatter Plot
# PART OF WHOLE?     → Pie Chart
# OUTLIERS/SPREAD?   → Box Plot
# CORRELATION/TABLE? → Heatmap