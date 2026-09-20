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
# Average attendance_pct by city — using horizontal bars, since city names can sometimes be long and this style is easier to scan.

# city_avg = df.groupby("city")["attendance_pct"].mean().sort_values(ascending=True)

# fig , ax = plt.subplots(figsize=(9,5.5))

# bars = ax.barh(
#     city_avg.index , 
#     city_avg.values,
#     color="#5a3434",
#     edgecolor = "white",
#     linewidth=1.2,
#     height=0.6,

# )
# for bar in bars:
#     width= bar.get_width()
#     ax.text(
#         width+0.5,
#         bar.get_y() + bar.get_height()/2,
#         f"{width:.1f}",
#         va="center",
#         fontsize=10,
#         fontweight="bold"
#     )

# ax.set_title("Average Attendance % by City",fontsize=14,fontweight="bold")
# ax.set_xlabel("Average Attendance (%)",fontsize=11)
# ax.set_ylabel("City",fontsize=11)

# ax.xaxis.grid(True,linestyle="--",alpha=0.6)
# ax.set_axisbelow(True)

# ax.set_xlim(0,city_avg.max() + 10)
# plt.tight_layout()
# plt.savefig("Horizontal Bar Plot.png")
# plt.show()

# Pie Chart :
# How students are split across fee_status (Paid, Unpaid, Pending) — as percentages of the whole.

# df["fee_status_clean"] = df["fee_status"].str.strip().str.lower()

# status_counts = df["fee_status_clean"].value_counts()
# fig,ax = plt.subplots(figsize=(7,7))
# wedges , texts , autotexts = ax.pie(
#     status_counts.values,
#     labels=status_counts.index,
#     autopct="%1.1f%%",
#     startangle=90,
#     colors=["#4C72B0","#DD8452","#55A868"],
#     explode = [0.05,0,0,0],
#     shadow=True,
#     wedgeprops={
#         "edgecolor":"white",
#         "linewidth": 2
#     }
# )

# for autotext in autotexts:
#     autotext.set_color("white")
#     autotext.set_fontweight("bold")
#     autotext.set_fontsize(11)
# for text in texts:
#     text.set_fontsize(11)

# ax.set_title("Fee Status Distribution",fontsize=14,fontweight="bold",color="Blue")

# ax.axis("equal")

# plt.tight_layout()
# plt.savefig("Pie Chart.png")
# plt.show()

# Histogram 
# How marks are spread out across all 200 students — are most students scoring average, high, or low?

# fig , ax =plt.subplots(figsize=(9,5.5))

# n,bins,patches = ax.hist(
#     df["marks"].dropna(),
#     bins=15,
#     color="#8172B2",
#     linewidth=1.2,
#     alpha=0.8,
#     rwidth=0.85
# )
# mean_marks = df["marks"].mean()

# ax.axvline(
#     mean_marks,
#     color="red",
#     linestyle="--",
#     linewidth=2,
#     label=f"Mean = {mean_marks:.1f}"
# )
# ax.set_title("Distribution of Student Marks",fontsize=14,fontweight="bold")

# ax.set_xlabel("Marks",fontsize=11)
# ax.set_ylabel("Number of Students",fontsize=11)

# ax.legend()

# ax.yaxis.grid(True,linestyle="--",alpha=0.75)
# ax.set_axisbelow(True)

# plt.tight_layout()
# plt.savefig("Histogram.png")
# plt.show()

#Scatter Plot 

# fig,ax=plt.subplots(figsize=(9,6))

# scatter=ax.scatter(
#     df["attendance_pct"],
#     df["marks"],
#     c=df["marks"],
#     cmap="viridis",
#     s=60,
#     alpha=0.75,
#     edgecolors="black",
#     linewidth=0.5
# )
# cbar= fig.colorbar(scatter , ax = ax)
# cbar.set_label("Marks",fontsize=10)

# ax.set_title("Attendance vs Marks",fontsize=15,color="orange")

# ax.set_xlabel("Attendance (%)",fontsize=11)
# ax.set_ylabel("Marks",fontsize=11)

# ax.grid(True,linestyle="--",alpha=0.4)
# plt.tight_layout()
# plt.savefig("Scatter_Plot.png")
# plt.show()

# Step Plot :
# df_sorted= df.sort_values("join_date")
# df_sorted["cumulative_students"] = range(1,len(df_sorted)+1)

# fig , ax = plt.subplots(figsize=(10,5.5))

# ax.step(df_sorted["join_date"],
#         df_sorted["cumulative_students"],
#         where="post",
#         color="#C44E52",
#         linewidth=2,
#         )
# ax.set_title("Cumulative Student Enrollment Over Time", fontsize=14, fontweight="bold")
# ax.set_xlabel("Join Date", fontsize=11)
# ax.set_ylabel("Total Students Enrolled", fontsize=11)
# ax.grid(True, linestyle="--", alpha=0.5)
# plt.xticks(rotation=30)                                     # tilt date labels so they don't overlap

# plt.tight_layout()
# plt.savefig("Step_Plots.png")
# plt.show()

# Stacked Bar Chart :
# Number of students per subject, stacked by fee_status (paid/unpaid/pending) — so we see both the total per subject AND the fee breakdown within each.

# df["fee_status_clean"] = df["fee_status"].str.strip().str.lower()

# pivot = pd.crosstab(df["subject"],df["fee_status_clean"])

# fig , ax = plt.subplots(figsize=(10,6))

# bottom = None 
# colors = {"paid": "#55A868","unpaid":"#C44E52","pending": "#2508DF"}

# for status in pivot.columns: 
#     values = pivot[status]
#     ax.bar(
#         pivot.index,
#         values,
#         bottom=bottom,
#         label=status,
#         color=colors.get(status,"gray"),
#         edgecolor="black",
#         linewidth=1
#     )
# bottom = values if bottom is None else bottom+values 


# ax.set_title("Students per Subject, split by Fee Status", fontsize=16,fontweight="bold")
# ax.set_xlabel("Subject",fontsize=11)
# ax.set_ylabel("Number of Students",fontsize=11)
# ax.legend(title="Fee Status")
# ax.yaxis.grid(True , linestyle="--",alpha=0.5)
# ax.set_axisbelow(True)
# plt.xticks(rotation=20)

# plt.tight_layout()
# plt.savefig("Stacked_Bar_Plot.png")
# plt.show()

# Area Plot 
#  Cumulative student enrollment over time — same data as the step plot, but now filled in to emphasize the "building up" feeling.


# df_sorted = df.sort_values("join_date")                          # sort earliest to latest join date
# df_sorted["cumulative_students"] = range(1, len(df_sorted) + 1)  # running total, same trick as step plot

# fig, ax = plt.subplots(figsize=(10, 5.5))

# ax.fill_between(df_sorted["join_date"],
#                 df_sorted["cumulative_students"],
#                 color="#4C72B0",
#                 alpha=0.4)

# ax.plot(df_sorted["join_date"],
# df_sorted["cumulative_students"],
# color="#4C72B0",
# linewidth=2)

# ax.set_title("Cumulative Student Enrollment", fontsize=16,fontweight="bold")
# ax.set_xlabel("Join Date", fontsize=11)
# ax.set_ylabel("Total Students Enrolled", fontsize=11)
# ax.grid(True, linestyle="--", alpha=0.5)
# plt.xticks(rotation=30)

# plt.tight_layout()
# plt.savefig("Area Plot.png")
# plt.show()

#Box Plot: Distribution of marks for each subject — comparing spread, median, and outliers across subjects.

# subjects =df["subject"].unique()
# data_per_subject = [df[df["subject"] == subj]["marks"].dropna() for subj in subjects]

# fig , ax = plt.subplots(figsize=(10,6))
# box = ax.boxplot(
#     data_per_subject,
#     tick_labels=subjects,
#     patch_artist=True,
#     medianprops=dict(color="black",linewidth=2),
#     flierprops=dict(marker="o",markerfacecolor="red",markersize=6 , markeredgecolor="black")
# )
# colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"]

# for patch , color in zip(box["boxes"],colors):
#     patch.set_facecolor(color)
#     patch.set_alpha(0.78)

# ax.set_title("Marks Distribution by Subject", fontsize=14, fontweight="bold")
# ax.set_xlabel("Subject", fontsize=11)
# ax.set_ylabel("Marks", fontsize=11)
# ax.yaxis.grid(True, linestyle="--", alpha=0.5)
# ax.set_axisbelow(True)
# plt.xticks(rotation=15)

# plt.tight_layout()
# plt.savefig("Box Plot.png")
# plt.show()


# Violin Plot:Same idea as the box plot — marks by subject — but showing the full shape of the distribution.

# Same trick as box plot: one list of marks per subject
# subjects = df["subject"].unique()
# data_per_subject = [df[df["subject"] == subj]["marks"].dropna() for subj in subjects]

# fig, ax = plt.subplots(figsize=(10, 6))


# violin=ax.violinplot(
#     data_per_subject,
#     showmedians=True,
#     # patch_artist=True,
#     # medianprops=dict(color="black",linewidth=2)
# )
# colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"] 
# for body , color in zip(violin["bodies"], colors):
#     body.set_facecolor(color)
#     body.set_edgecolor("black")
#     body.set_alpha(0.7)
# ax.set_xticks(range(1,len(subjects)+1))
# ax.set_xticklabels(subjects)


# ax.set_title("Marks Distribution by Subject (Violin Plot)", fontsize=14, fontweight="bold")
# ax.set_xlabel("Subject", fontsize=11)
# ax.set_ylabel("Marks", fontsize=11)
# ax.grid(True, linestyle="--", alpha=0.5)

# plt.tight_layout()
# plt.savefig("Violin Plot.png", dpi=150)
# plt.show()

# Error Plot 
# Average marks per subject, with error bars showing how much marks vary (standard deviation) within each subject.

# grouped = df.groupby("subject")["marks"].agg(["mean","std"])

# fig , ax = plt.subplots(figsize=(9,6))

# ax.errorbar(
#     grouped.index , 
#     grouped["mean"],
#     yerr=grouped["std"],
#     fmt="o",
#     color="#4c72B0",
#     ecolor="black",
#     elinewidth=2,
#     capsize=6,
#     markersize=8
# )
# ax.set_title("Average Marks by Subject (with Variation)", fontsize=14, fontweight="bold")
# ax.set_xlabel("Subject", fontsize=11)
# ax.set_ylabel("Marks", fontsize=11)
# ax.grid(True, linestyle="--", alpha=0.5)

# plt.tight_layout()
# plt.savefig("Error Plot.png")
# plt.show()

# Stem Plot :Marks for the first 20 students — as separate, individual lollipops (not connected), since each student's mark is its own independent data point.

# first_20 = df.head(20)

# fig,ax = plt.subplots(figsize=(11,5.5))

# ax.stem(
#     first_20["student_id"],
#     first_20["marks"],
#     linefmt="#4C72B0",
#     markerfmt="s",
#     basefmt="black"
# )
# ax.set_title("Marks of First 20 Students (Stem Plot)", fontsize=14, fontweight="bold")
# ax.set_xlabel("Student ID", fontsize=11)
# ax.set_ylabel("Marks", fontsize=11)
# ax.grid(True, linestyle="--", alpha=0.5)

# plt.tight_layout()
# plt.savefig("Stem Plot.png")
# plt.show()

# Heatmap
# A correlation matrix — checking how numeric columns (age, marks, attendance_pct) relate to each other.

# numeric_cols = df[["age","marks","attendance_pct"]]
# corr = numeric_cols.corr()

# fig , ax = plt.subplots(figsize=(7,6))
# im = ax.imshow(corr , cmap="coolwarm", vmin=-1,vmax=1)

# cbar = fig.colorbar(im,ax=ax)
# cbar.set_label("Correlation",fontsize=11)

# ax.set_xticks(range(len(corr.columns)))
# ax.set_xticklabels(corr.columns)
# ax.set_yticks(range(len(corr.columns)))
# ax.set_yticklabels(corr.columns)

# for i in range(len(corr.columns)):
#     for j in range(len(corr.columns)):
#         ax.text(
#             j,i,
#             f"{corr.iloc[i,j]:.2f}",
#             ha="center",
#             va="center",
#             color="black",
#             fontweight="bold"
#         )

# ax.set_title("Correlation Heatmap", fontsize=14, fontweight="bold")

# plt.tight_layout()
# plt.savefig("HeatMap Plot.png")
# plt.show()

# Missing Value HeatMap:
# Where our dataset has missing (NaN) values, using a simple 2-color grid.

# missing = df.isnull()
# print(missing.sum())

# fig , ax = plt.subplots(figsize=(9,10))

# ax.imshow(missing , cmap="viridis", aspect="auto")
# ax.set_xticks(range(len(df.columns)))
# ax.set_xticklabels(df.columns , rotation=45,ha="right")
# ax.set_ylabel("Row Number (Student)", fontsize=11)


# ax.set_title("Missing Values Heatmap (Yellow = Missing)", fontsize=14, fontweight="bold")

# plt.tight_layout()
# plt.savefig("Missing Value HeatMap.png")
# plt.show()

# 2D Histogram : Density of students across attendance_pct vs marks — using colored squares to show where students cluster, instead of a busy scatter plo

# fig , ax = plt.subplots(figsize=(8,6.5))
# h = ax.hist2d(df["attendance_pct"],
#               df["marks"].dropna(),
#               bins=15,
#               cmap="plasma")

# cbar = fig.colorbar(h[3],ax=ax)
# cbar.set_label("Number of Students", fontsize=11)
# ax.set_title("Attendance vs Marks Density (2D Histogram)", fontsize=14, fontweight="bold")
# ax.set_xlabel("Attendance (%)", fontsize=11)
# ax.set_ylabel("Marks", fontsize=11)

# plt.tight_layout()
# plt.savefig("Histogram2D.png")
# plt.show()

# # Pseudocolor Plot:
# # Bin attendance and marks into groups, then find average marks per (attendance bin, subject) cell
# df["att_bin"] = pd.cut(df["attendance_pct"], bins=6)          # split attendance into 6 ranges
# pivot = df.pivot_table(values="marks", index="subject", columns="att_bin", observed=False)  # avg marks grid

# fig, ax = plt.subplots(figsize=(10, 6))

# mesh = ax.pcolormesh(pivot.values, cmap="YlOrRd", edgecolors="white", linewidth=1)  # draw uneven-ready grid

# ax.set_xticks(np.arange(len(pivot.columns)) + 0.5)             # center tick labels on each cell
# ax.set_xticklabels([str(c) for c in pivot.columns], rotation=45, ha="right")
# ax.set_yticks(np.arange(len(pivot.index)) + 0.5)
# ax.set_yticklabels(pivot.index)

# fig.colorbar(mesh, ax=ax, label="Average Marks")
# ax.set_title("Average Marks: Subject vs Attendance Range", fontsize=14, fontweight="bold")

# plt.tight_layout()
# plt.savefig("Pseducolor Plot.png")
# plt.show()

#Hexbin Plot

# fig ,ax = plt.subplots(figsize=(8,6.5))
# hb = ax.hexbin(
#     df["attendance_pct"],
#     df["marks"],
#     gridsize=20,
#     cmap="viridis"
# )

# fig.colorbar(hb , ax = ax , label = "Number of Students")
# ax.set_title("Attendance vs Marks (Hexbin)", fontsize=14, fontweight="bold")
# ax.set_xlabel("Attendance (%)", fontsize=11)
# ax.set_ylabel("Marks", fontsize=11)
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
# plt.tight_layout()
# plt.savefig("Hexabin Plot.png")
# plt.show()


# Pair Plot 

# cols = ["age","marks","attendance_pct"]

# fig , axes = plt.subplots(len(cols),len(cols),figsize=(9,9))

# for i , col_y in enumerate(cols):
#     for j , col_x in enumerate(cols):
#         ax = axes[i,j]
#         if i==j:
#             ax.hist(df[col_x].dropna(),color="#55A868")
#         else:
#             ax.scatter(df[col_x],df[col_y],s=10,alpha=0.5, color="#4C72B0")
#         if i == len(cols)-1:
#             ax.set_xlabel(col_x)
#         if j== 0:
#             ax.set_ylabel(col_y)

# fig.suptitle("Pair Plot of Numeric Columns", fontsize=14, fontweight="bold")
# plt.tight_layout()
# plt.savefig("Pair Plot.png")
# plt.show()

# 3D Scatter Plot:
# fig= plt.figure(figsize=(9,7))
# ax = fig.add_subplot(111, projection="3d")

# sc = ax.scatter(
#     df["age"],
#     df["attendance_pct"],
#     df["marks"],
#     c=df["marks"],
#     cmap="viridis",
#     s=40
# )

# ax.set_xlabel("Age")
# ax.set_ylabel("Attendance (%)")
# ax.set_zlabel("Marks")
# ax.set_title("Age vs Attendance vs Marks (3D)", fontsize=14, fontweight="bold")
# fig.colorbar(sc, ax=ax, shrink=0.6, label="Marks")

# plt.tight_layout()
# plt.savefig("3D Scatter Plot.png")
# plt.show()

# # CDF Plot : 
# marks_sorted = np.sort(df["marks"].dropna())
# cdf_values = np.arange(1,len(marks_sorted) +1)/len(marks_sorted)*100

# fig , ax = plt.subplots(figsize=(9,5.5))

# ax.plot(marks_sorted,cdf_values,color="#4C72B0",linewidth=2)
# ax.set_title("Cumulative Distribution of Marks (CDF)", fontsize=14, fontweight="bold")
# ax.set_xlabel("Marks", fontsize=11)
# ax.set_ylabel("% of Students Scoring This or Below", fontsize=11)
# ax.grid(True, linestyle="--", alpha=0.5)

# plt.tight_layout()
# plt.savefig("CDF_Plot.png")
# plt.show()

# Frequency Polygon:


# marks = df["marks"].dropna()
# fig , ax = plt.subplots(figsize=(9,5.5))
# counts , bin_edges= np.histogram(marks,bins=15)
# bin_centers = (bin_edges[:-1]+ bin_edges[1:]) /2

# ax.plot(bin_centers,counts , alpha=0.2 ,color="#C44E52",linewidth=2)

# ax.set_title("Frequency Polygon of Marks", fontsize=14, fontweight="bold")
# ax.set_xlabel("Marks", fontsize=11)
# ax.set_ylabel("Number of Students", fontsize=11)
# ax.grid(True, linestyle="--", alpha=0.5)

# plt.tight_layout()
# plt.savefig("Frequency_Polygon Plot")
# plt.show()

#Bubble Plot
# fig, ax = plt.subplots(figsize=(9, 6.5)) 
# # bubble size needs to be scaled up, since raw values (like attendance %) are too small to see as dot sizes
# bubble_sizes = df["attendance_pct"] * 3  # multiply so bubbles are big enough to actually see differences

# scatter = ax.scatter(
#     df["age"],                # X-axis: age
#     df["marks"],              # Y-axis: marks
#     s=bubble_sizes,           # SIZE of each dot comes from attendance (3rd variable!)
#     c=df["marks"],            # color also shows marks, for extra clarity
#     cmap="cool",
#     alpha=0.6,                # see-through, so overlapping bubbles are still visible
#     edgecolors="black",
#     linewidth=0.7
# )

# fig.colorbar(scatter, ax=ax, label="Marks")

# ax.set_title("Age vs Marks (Bubble Size = Attendance %)", fontsize=14, fontweight="bold")
# ax.set_xlabel("Age", fontsize=11)
# ax.set_ylabel("Marks", fontsize=11)
# ax.grid(True, linestyle="--", alpha=0.4)

# plt.tight_layout()
# plt.savefig("Bubble Plot.png")
# plt.show()

#Rug Plot
# marks = df["marks"].dropna()

# fig, ax = plt.subplots(figsize=(9, 5.5))

# # draw the histogram like normal, for context
# ax.hist(marks, bins=15, color="#4C72B0", edgecolor="black", alpha=0.6, rwidth=0.9)

# # now add the rug: one small vertical tick per actual data point, sitting near the bottom
# ax.plot(
#     marks,                     # X position: the actual mark value for each student
#     [-1] * len(marks),         # put every tick at the SAME low Y position, just below the bars
#     "|",                       # marker shape: a vertical tick mark (looks like a pipe symbol)
#     color="black",
#     markersize=15,             # how tall each tick mark is
#     markeredgewidth=1          # thickness of each tick mark
# )

# ax.set_title("Marks Histogram with Rug Plot", fontsize=14, fontweight="bold")
# ax.set_xlabel("Marks", fontsize=11)
# ax.set_ylabel("Number of Students", fontsize=11)
# ax.grid(True, linestyle="--", alpha=0.5)

# plt.tight_layout()
# plt.savefig("Rug Plot.png")
# plt.show()

#Grouped Bar Chart:
df["fee_status_clean"] = df["fee_status"].str.strip().str.lower()

# Same cross-tab as our stacked bar chart
pivot = pd.crosstab(df["subject"], df["fee_status_clean"])

fig, ax = plt.subplots(figsize=(11, 6))

n_statuses = len(pivot.columns)          # how many fee statuses (bars per group) - here, 3
bar_width = 0.25                         # width of each individual bar
x = np.arange(len(pivot.index))          # base positions for each subject group: 0,1,2,3,4

colors = ["#55A868", "#DD8452", "#C44E52", "#8172B2"]

for i, status in enumerate(pivot.columns):          # loop through paid, pending, unpaid (i = 0, 1, 2)
    # shift each status's bars slightly left/right, so they sit side by side, not on top of each other
    offset = (i - n_statuses/2) * bar_width + bar_width/2
    ax.bar(
        x + offset,                     # shifted X position for THIS status's bars
        pivot[status],                  # heights: counts for this status, across all subjects
        width=bar_width,
        label=status,
        color=colors[i % len(colors)],
        edgecolor="black"
    )

ax.set_xticks(x)
ax.set_xticklabels(pivot.index, rotation=15)

ax.set_title("Students per Subject, Grouped by Fee Status", fontsize=14, fontweight="bold")
ax.set_xlabel("Subject", fontsize=11)
ax.set_ylabel("Number of Students", fontsize=11)
ax.legend(title="Fee Status")
ax.yaxis.grid(True, linestyle="--", alpha=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig("Grouped Bar Chart.png")
plt.show()