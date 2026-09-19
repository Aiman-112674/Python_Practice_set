#dataset
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Pandas_Library\Clean_Full_Practice_Dataset.csv" , parse_dates=["join_date"])

print("Columns:", df.columns.tolist())

print(df.isna().sum())
df["attendance_pct"] = df["attendance_pct"].fillna(df["attendance_pct"].mean())
print(df.isna().sum())

# Line Plot 
# Average marks over time — grouped by join_date (month), to see if student performance trends up or down over time.
df["join_month"] = df["join_date"].dt.to_period("M")
monthly_avg = df.groupby("join_month")["marks"].mean()
monthly_avg = monthly_avg.sort_index()

# plotting the graph 
fig,ax = plt.subplots(figsize=(10,5))
ax.plot(monthly_avg.index.astype(str),monthly_avg.values,marker ="o" , linestyle="-",color="#4C72B0",linewidth=2,markersize=6
)

ax.set_title("Average Student Marks Over Time",fontsize=14,fontweight="bold",color="black")

ax.set_xlabel("Join Month",fontsize=11)
ax.set_ylabel("Average Marks", fontsize=11)
ax.grid(True,linestyle="--",alpha=0.6)
ax.set_facecolor("#ffeeee")
plt.xticks(rotation=45)
plt.tight_layout()
# plt.savefig("line_plot.png")
plt.show()

# Assigment of Line plot
# Goal: Plot the average attendance_pct over time, grouped by join_month (just like we did with marks, but now with a different column).
# df["join_month"] = df["join_date"].dt.to_period("M")
monthly_avg_attendance = df.groupby("join_month")["attendance_pct"].mean()
monthly_avg_attendance = monthly_avg_attendance.sort_index()
# plotthing 
fig,ax = plt.subplots(figsize=(9,5))
ax.plot(monthly_avg_attendance.index.astype(str),monthly_avg_attendance.values,marker="s",linestyle="-.",linewidth=2,color="#15ffdcdd",markersize=6)

ax.set_title("Average Student Attendance over time",fontsize=16,fontweight="bold",color="red")
ax.grid(True,linestyle=":",alpha=0.6)
ax.set_facecolor("#fef998")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("Line_plot2.png")
plt.show()
