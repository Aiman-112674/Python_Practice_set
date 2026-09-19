#dataset
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Pandas_Library\Clean_Full_Practice_Dataset.csv" , parse_dates=["join_date"])

print("Columns:", df.columns.tolist())

print(df.isna().sum())
df["attendance_pct"] = df["attendance_pct"].fillna(df["attendance_pct"].mean())
print(df.isna().sum())

# # Line Plot 
# # Average marks over time — grouped by join_date (month), to see if student performance trends up or down over time.
# df["join_month"] = df["join_date"].dt.to_period("M")
# monthly_avg = df.groupby("join_month")["marks"].mean()
# monthly_avg = monthly_avg.sort_index()

# # plotting the graph 
# fig,ax = plt.subplots(figsize=(10,5))
# ax.plot(monthly_avg.index.astype(str),monthly_avg.values,marker ="o" , linestyle="-",color="#4C72B0",linewidth=2,markersize=6
# )

# ax.set_title("Average Student Marks Over Time",fontsize=14,fontweight="bold",color="black")

# ax.set_xlabel("Join Month",fontsize=11)
# ax.set_ylabel("Average Marks", fontsize=11)
# ax.grid(True,linestyle="--",alpha=0.6)
# ax.set_facecolor("#ffeeee")
# plt.xticks(rotation=45)
# plt.tight_layout()
# # plt.savefig("line_plot.png")
# plt.show()

# # Assigment of Line plot
# # Goal: Plot the average attendance_pct over time, grouped by join_month (just like we did with marks, but now with a different column).
# # df["join_month"] = df["join_date"].dt.to_period("M")
# monthly_avg_attendance = df.groupby("join_month")["attendance_pct"].mean()
# monthly_avg_attendance = monthly_avg_attendance.sort_index()
# # plotthing 
# fig,ax = plt.subplots(figsize=(9,5))
# ax.plot(monthly_avg_attendance.index.astype(str),monthly_avg_attendance.values,marker="s",linestyle="-.",linewidth=2,color="#15ffdcdd",markersize=6)

# ax.set_title("Average Student Attendance over time",fontsize=16,fontweight="bold",color="red")
# ax.grid(True,linestyle=":",alpha=0.6)
# ax.set_facecolor("#fef998")
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)

# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.savefig("Line_plot2.png")
# plt.show()

# # Bar Plot --Average marks by subject — comparing performance across the 5 subjects.

# subject_avg = df.groupby("subject")["marks"].mean().sort_values(ascending=False)

# fig,ax = plt.subplots(figsize=(9,5.5))

# # bar chart 

# bars = ax.bar(
#     subject_avg.index,
#     subject_avg.values,
#     color="#04691B",
#     edgecolor="pink",
#     linewidth=1.2,
#     width=0.6
# )
# for bar in bars:
#     height = bar.get_height()
#     ax.text(
#         bar.get_x() + bar.get_width()/2,
#         height+0.5,
#         f"{height:.1f}",
#         ha="center",
#         fontsize=10,
#         fontweight="bold"
#     )

# ax.set_title("Average Marks by Subject",fontsize=14,fontweight=16)
# ax.set_xlabel("Subject",fontsize=11)
# ax.set_ylabel("Average Marks",fontsize=11)
# ax.yaxis.grid(True,linestyle="--",alpha=0.6)
# ax.set_axisbelow(True)
# ax.set_ylim(0,subject_avg.max()+10)
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
# ax.set_facecolor("#cff0ff")
# plt.tight_layout()
# plt.savefig("Bar_Plot.png")
# plt.show()

# # Bar Plot Assignment :Plot the average attendance_pct by fee_status (Paid, Unpaid, Pending) as a bar chart — to see if students who pay on time also tend to attend more.

# visualizing_attendance = df.groupby("fee_status")["attendance_pct"].mean().sort_values(ascending=False)

# fig ,ax = plt.subplots(figsize=(9,5))

# bars=ax.bar(
#     visualizing_attendance.index,
#     visualizing_attendance.values,
#     color="#8222f8",
#     edgecolor="white",
#     linewidth=1.2,
#     width=0.6
# )
# for bar in bars:
#     height=bar.get_height()
#     ax.text(
#         bar.get_x() + bar.get_width()/2,
#         height+0.5,
#         f"{height:.1f}",
#         ha="center",
#         fontsize=12,
#         fontweight="bold"
#     )

# ax.set_title("Avg Attendance by Fee Status")
# ax.set_xlabel("Fee Status")
# ax.set_ylabel("Avg Attendance")
# ax.yaxis.grid(True,linestyle="-",alpha=0.6)
# ax.set_axisbelow(True)
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
# ax.set_facecolor("#ACCBEF")
# plt.tight_layout()

# plt.savefig("Bar_Plot2.png")
# plt.show()

# Horizontal Bar Plot:

visualizing_city_attendance= df.groupby("city")["attendance_pct"].mean().sort_values(ascending=False)

fig,ax = plt.subplots(figsize=(9,5))

barhs = ax.barh(visualizing_city_attendance.index,
                visualizing_city_attendance.values,
                color="#864747",
                edgecolor="skyblue",
                linewidth=1.2,
                height=0.75,)

for bar in barhs :
    width = bar.get_width()
    # ax.text(
    #     width,ax.get_fc() + ax.get_height()/2,
    #     # height+0.5,
    #     f"{width:.1f}",
    #     ha="left",
    #     va="center",
    #     fontweigt="bold",
    #     fontsize=14
    # )
    ax.annotate(
        f"{width:.1f}",
        xy=(width , bar.get_y()+ bar.get_height()/2),
        xytext=(5,0),
        textcoords="offset points",
        ha="left",
        va="center",
        fontsize=12,
        fontweight="bold"
    )

ax.set_title("Average Attedance of Students in each City",fontsize=16,fontweight="bold",color="purple")
ax.set_xlabel("Attendance",fontsize=12,fontweight="bold")
ax.set_ylabel("City",fontsize=12,fontweight="bold")
ax.xaxis.grid(True,linestyle="-",alpha=0.7)
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_facecolor("#FAF0F9")
plt.tight_layout()

plt.savefig("Horizontal_Bar_Plot.png")
plt.show()

