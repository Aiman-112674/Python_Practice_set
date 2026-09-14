import matplotlib.pyplot as plt
import numpy as np 

student_name = ["Ali","Zain","Sara","Nisa","Nida","Usman","Hinsa"]
student_age = [19,18,17,19,16,21,20]

fig , ax = plt.subplots()
ax.plot(student_name,student_age,color="green",marker="^",markersize=10,markerfacecolor="orange",markeredgecolor="black",linestyle="-",linewidth=3)
# Grid Lines 
ax.grid(True,linestyle=":",alpha=0.6)
#Font Sizes and styling for title/ Labels 

ax.set_xlabel("Names of Student",fontsize=13)
ax.set_ylabel("Ages of Student",fontsize=12)
ax.set_title("Student Detail",fontsize = 16 ,fontweight="bold",color = "darkgreen")
# setting axis range 
ax.set_ylim(0,22)

# label individual data points (show the actual value near each point)
for i , age in enumerate(student_age):
    ax.annotate(str(age),(student_name[i],age), textcoords="offset points",xytext=(0,10),ha="center")
#annotate() writes a text label at a chosen position; textcoords="offset points" + xytext=(0,10) nudges that text slightly away from the exact data point (10 points upward here) so it doesn't overlap the dot; ha="center" keeps the text horizontally centered on that point.

#Background color of the plot area 
ax.set_facecolor("#ecedec")
fig.patch.set_facecolor("white")


# addding a horizontal reference line 
import numpy as np 
avg_age = np.mean(student_age)
median_age = np.median(student_age)
ax.axhline(avg_age,color ="red",linestyle="-.",linewidth=1,label =f"Average Age: {avg_age:.1f}")
ax.axhline(median_age,color ="blue",linestyle="--",linewidth=1.5,label =f"Median Age: {median_age:.1f}")
ax.legend()
# ax.scatter(student_name,student_age,marker="o",s=200,zorder=10)
#setting figure size
fig.set_size_inches(8,5)
# remove unnecessary borders 
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.show()
#One-sentence summary

# ax is your entire toolbox (the plot area) — .plot(), .axhline(), .grid(), .bar() etc. are all DIFFERENT tools inside that same toolbox, each doing a different specific job. You used .plot() to draw your actual data, and .axhline() separately to draw an extra horizontal reference line at the average — both can exist together on the same chart, layered on top of each other.

# multiple axes side by side inside one figure 

student_name = ["Ali","Zain","Sara","Nisa","Nida","Usman","Hinsa"]
student_age = [19,18,17,19,16,21,20]
student_marks = [80,65,90,72,88,55,95]

fig , ax = plt.subplots(1,2,figsize = (12,6))

#first subplot
ax[0].plot(student_name,student_age,marker="*",color="green")

ax[0].set_title("Student Ages")
ax[0].set_xlabel("Name")
ax[0].set_ylabel("Age")

# second plot 

ax[1].bar(student_name,student_marks,color ="skyblue")
ax[1].set_title("Student Marks")
ax[1].set_xlabel("Name")
ax[1].set_ylabel("Marks")
# avoiding the overlapping 
ax[1].tick_params(axis="x",rotation = 30)

plt.show()


# Multiple Axes inside one figure 

fig , ax = plt.subplots(2,2,figsize=(17,7))
# 1st plot
ax[0,0].plot(student_name,student_age,marker="*", markerfacecolor="green")
ax[0,0].set_title("line Plot")
ax[0,0].set_xlabel("Name")
ax[0,0].set_ylabel("Age")
ax[0,0].grid(True,linestyle=":",alpha=0.6)
#2nd plot
ax[0,1].bar(student_name,student_marks,color="yellow",edgecolor="black")
ax[0,1].set_title("Bar Plot")
ax[0,1].set_xlabel("Name")
ax[0,1].set_ylabel("Marks")
ax[0,1].grid(True,linestyle=":",alpha=0.1)

# 3rd plot 

ax[1,0].hist(student_marks,bins=2,color="orange")
ax[1,0].set_title("Histogram Plot")
ax[1,0].set_xlabel("Marks")
ax[1,0].grid(True,linestyle=":",alpha=0.9)

# 4th plot

ax[1,1].scatter(student_age , student_marks)
ax[1,1].set_title("Scatter Plot")
ax[1,1].set_xlabel("Age")
ax[1,1].set_ylabel("Marks")
ax[1,1].grid(True,linestyle=":",alpha=0.6)
plt.tight_layout()
plt.show()