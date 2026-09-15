# import matplotlib.pyplot as plt
# import numpy as np 

# student_name = ["Ali","Zain","Sara","Nisa","Nida","Usman","Hinsa"]
# student_age = [19,18,17,19,16,21,20]

# fig , ax = plt.subplots()
# ax.plot(student_name,student_age,color="green",marker="^",markersize=10,markerfacecolor="orange",markeredgecolor="black",linestyle="-",linewidth=3)
# # Grid Lines 
# ax.grid(True,linestyle=":",alpha=0.6)
# #Font Sizes and styling for title/ Labels 

# ax.set_xlabel("Names of Student",fontsize=13)
# ax.set_ylabel("Ages of Student",fontsize=12)
# ax.set_title("Student Detail",fontsize = 16 ,fontweight="bold",color = "darkgreen")
# # setting axis range 
# ax.set_ylim(0,22)

# # label individual data points (show the actual value near each point)
# for i , age in enumerate(student_age):
#     ax.annotate(str(age),(student_name[i],age), textcoords="offset points",xytext=(0,10),ha="center")
# #annotate() writes a text label at a chosen position; textcoords="offset points" + xytext=(0,10) nudges that text slightly away from the exact data point (10 points upward here) so it doesn't overlap the dot; ha="center" keeps the text horizontally centered on that point.

# #Background color of the plot area 
# ax.set_facecolor("#ecedec")
# fig.patch.set_facecolor("white")


# # addding a horizontal reference line 
# import numpy as np 
# avg_age = np.mean(student_age)
# median_age = np.median(student_age)
# ax.axhline(avg_age,color ="red",linestyle="-.",linewidth=1,label =f"Average Age: {avg_age:.1f}")
# ax.axhline(median_age,color ="blue",linestyle="--",linewidth=1.5,label =f"Median Age: {median_age:.1f}")
# ax.legend()
# # ax.scatter(student_name,student_age,marker="o",s=200,zorder=10)
# #setting figure size
# fig.set_size_inches(8,5)
# # remove unnecessary borders 
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)

# plt.show()
# #One-sentence summary

# # ax is your entire toolbox (the plot area) — .plot(), .axhline(), .grid(), .bar() etc. are all DIFFERENT tools inside that same toolbox, each doing a different specific job. You used .plot() to draw your actual data, and .axhline() separately to draw an extra horizontal reference line at the average — both can exist together on the same chart, layered on top of each other.

# # multiple axes side by side inside one figure 

# student_name = ["Ali","Zain","Sara","Nisa","Nida","Usman","Hinsa"]
# student_age = [19,18,17,19,16,21,20]
# student_marks = [80,65,90,72,88,55,95]

# fig , ax = plt.subplots(1,2,figsize = (12,6))

# #first subplot
# ax[0].plot(student_name,student_age,marker="*",color="green")

# ax[0].set_title("Student Ages")
# ax[0].set_xlabel("Name")
# ax[0].set_ylabel("Age")

# # second plot 

# ax[1].bar(student_name,student_marks,color ="skyblue")
# ax[1].set_title("Student Marks")
# ax[1].set_xlabel("Name")
# ax[1].set_ylabel("Marks")
# # avoiding the overlapping 
# ax[1].tick_params(axis="x",rotation = 30)

# plt.show()


# # Multiple Axes inside one figure 

# fig , ax = plt.subplots(2,2,figsize=(17,7))
# # 1st plot
# ax[0,0].plot(student_name,student_age,marker="*", markerfacecolor="green")
# ax[0,0].set_title("line Plot")
# ax[0,0].set_xlabel("Name")
# ax[0,0].set_ylabel("Age")
# ax[0,0].grid(True,linestyle=":",alpha=0.6)
# #2nd plot
# ax[0,1].bar(student_name,student_marks,color="yellow",edgecolor="black")
# ax[0,1].set_title("Bar Plot")
# ax[0,1].set_xlabel("Name")
# ax[0,1].set_ylabel("Marks")
# ax[0,1].grid(True,linestyle=":",alpha=0.1)

# # 3rd plot 

# ax[1,0].hist(student_marks,bins=2,color="orange")
# ax[1,0].set_title("Histogram Plot")
# ax[1,0].set_xlabel("Marks")
# ax[1,0].grid(True,linestyle=":",alpha=0.9)

# # 4th plot

# ax[1,1].scatter(student_age , student_marks)
# ax[1,1].set_title("Scatter Plot")
# ax[1,1].set_xlabel("Age")
# ax[1,1].set_ylabel("Marks")
# ax[1,1].grid(True,linestyle=":",alpha=0.6)
# plt.tight_layout()
# plt.show()

#  Plotting on File : 
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Pandas_Library\Clean_Full_Practice_dataset_By_using_KNN_Imputer.csv")

# 1st Gender/Category Percentage --Pie Chart

counts = df["fee_status"].value_counts()

fig , ax = plt.subplots()
ax.pie(counts , labels=counts.index , autopct="%1.1f%%")
ax.set_title("Fee Status Distribution")
plt.show()

# Histogram of Age 
# fig , ax = plt.subplots()
# ax.hist(["age"],bins=10,color="skyblue",edgecolor="black")
# ax.set_title("Age Distribution")
# ax.set_xlabel("Age")
# ax.set_ylabel("Number of Students")
# plt.show()

avg_marks = df.groupby("subject")["marks"].mean()
fig , ax = plt.subplots()
ax.bar(avg_marks.index,avg_marks.values , color="orange")

ax.set_title("Average Marks per Subject")
ax.set_xlabel("Subject")
ax.set_ylabel("Average Marks")
plt.xticks(rotation=30)
plt.show()


# Scatter plot 
fig, ax = plt.subplots()
ax.scatter(df["attendance_pct"], df["marks"], alpha=0.6, color="purple")
ax.set_title("Marks vs Attendance")
ax.set_xlabel("Attendance %")
ax.set_ylabel("Marks")
plt.show()

# Box Plot
# fig, ax = plt.subplots()
# ax.boxplot([df["age"].dropna(), df["marks"].dropna()])
# ax.set_title("Age and Marks Spread")

# plt.show()

# Line Plot 

fig , ax = plt.subplots()
ax.plot(df["subject"],df["marks"], color = "green", linestyle="-." ,linewidth=3 , label="Age",marker="^",markerfacecolor="orange")
ax.set_title("Student Age")
ax.set_xlabel("Name")
ax.set_ylabel("Age")
ax.legend()
plt.xticks(rotation=30)
plt.show()


# Bar Plot 
fig , ax = plt.subplots()
ax.bar(df["subject"],df["marks"],color="red",width=0.8)
ax.grid(True,alpha=0.6,linestyle=":")
ax.set_facecolor("yellow")
ax.set_title("Subject vs Marks", fontsize=13,fontstyle="italic")
ax.set_xlabel("Subject")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# ax.set_xticks(rotation=30)
ax.set_ylabel("Marks")
plt.xticks(rotation=30)
plt.show()

# Scatter Plot 

fig ,ax = plt.subplots()

ax.scatter(df["marks"],df["attendance_pct"],marker ="*",s=100,label="Attendance_Pct")
ax.set_facecolor("red")
ax.set_title("Relationship Analyzing between Marks & Attendance_Pct",fontstyle="italic",fontsize=14)
ax.set_xlabel("Marks")
ax.set_ylabel("Attendance_Pct")
ax.spines["top"].set_visible("False")
ax.spines["right"].set_visible("False")
ax.grid(True,linestyle=":",alpha=0.9)

# import numpy as np 
# avg_attendance= np.mean("attendance_pct")
# ax.axhline(avg_attendance,color="black",linestyle="-.",linewidth=0.9,label=f"Average Attendance: {avg_attendance:.1f}")
plt.xticks(rotation=30)
plt.show()

# Bar Plot -- city & attendance pct 

fig , ax = plt.subplots()
ax.bar(df["city"],df["attendance_pct"],color="white",edgecolor="black",linewidth=1.5,width=0.55,hatch=".",alpha=0.9)
# ax.bar_label(ba,padding=3,fontsize=10,fontweight="bold")
ax.set_facecolor("red")
ax.grid(True,linestyle=":",alpha=0.9)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_title("City & Attendance_Pct")
ax.set_xlabel("City")
ax.set_ylabel("Attendance_Pct")

plt.xticks(rotation=30)

plt.show()


#Scatter Plot 

fig , ax = plt.subplots()
ax.scatter(df["age"],df["marks"] , marker="D" , alpha=0.9,color="red",edgecolors="black",linestyle="-.",linewidth=0.8)
ax.set_title("Age vs Marks")
ax.set_xlabel("Age")
ax.set_ylabel("Marks")
ax.grid(True , linestyle=":" , alpha=0.9)

plt.xticks(rotation=30)
plt.show()


# Scatter plot with full Styling :
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig , ax = plt.subplots(figsize=(9,6))
scatter = ax.scatter(df["attendance_pct"],df["marks"], c=df["marks"],cmap="viridis",s=150,edgecolors="black",linewidth=1,alpha=0.85)


# trendline 

z = np.polyfit(df["attendance_pct"],df["marks"],1)
p = np.poly1d(z)
ax.plot(df["attendance_pct"],p(df["attendance_pct"]),color="red",linestyle="--",linewidth=2,label="Trend Line")

# Average Reference Line 

avg_marks = np.mean(df["marks"])
ax.axhline(avg_marks,color="gray",linestyle=":",linewidth=1.2,label=f"Avg Marks: {avg_marks:.1f}")

# Highlight the highest point

max_idx = df["marks"].idxmax()
ax.annotate(f"Highest: {df["marks"][max_idx]}",
            (df["attendance_pct"][max_idx],df["marks"][max_idx]),
            textcoords="offset points" , xytext = (10,10),
            fontsize=10,fontweight="bold",color="green")

fig.colorbar(scatter, ax = ax , label ="Marks")

ax.set_title("Attendance vs Marks", fontsize=16 , fontweight="bold", color = "red")
ax.set_xlabel("Attendance % ", fontsize=12)
ax.set_ylabel("Marks", fontsize=12)
ax.grid(True,linestyle=":",alpha=0.4)
ax.set_facecolor("#f9f9f9")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend()
print(df["attendance_pct"].corr(df["marks"]))
plt.tight_layout()
plt.show()


# Histogram with Styling 

import matplotlib.pyplot as plt 
import numpy as np 

fig , ax = plt.subplots(figsize=(9,6))

# histogram

n, bins_edges , patches = ax.hist(df["marks"] , bins =12,color="mediumseagreen" , edgecolor="black" , linewidth=1.2,alpha=0.85 ) 

# mean and median reference line 

mean_marks = np.mean(df["marks"])
median_marks = np.median(df["marks"])

ax.axvline(mean_marks , color ="red",linestyle="--",linewidth=2,label = f"Mean: {mean_marks:.1f}")

ax.axvline(median_marks , color ="blue",linestyle="--",linewidth=2,label=f"Median: {median_marks:.1f}")

# color : 

tallest_idx = np.argmax(n)
smallest_idx= np.argmin(n)
patches[tallest_idx].set_facecolor("orange")
patches[smallest_idx].set_facecolor("red")

# Add count labels on top of each bar 

for count , edge in zip(n , bins_edges):
    if count>0:
        ax.text(edge+ (bins_edges[1]-bins_edges[0])/2 , count+0.3 , int(count),
        ha = "center",fontsize=9, fontweight="bold" )

#titles and labels

ax.set_title("Distribution of Marks",fontsize=16, fontweight="bold" , color="darkgreen")
ax.set_xlabel("Marks", fontsize = 12)
ax.set_ylabel("Number of Students",fontsize=12)

# grid 
ax.grid(True,linestyle=":",alpha=0.4)
ax.set_facecolor("#f9f9f9")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.legend()
plt.tight_layout()
plt.show()