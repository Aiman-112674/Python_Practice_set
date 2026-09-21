# Count Plot

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv(r"C:\Users\fast laptop\Desktop\python_intern\Pandas_Library\Clean_Full_Practice_Dataset.csv")
df["attendance_pct"] = df["attendance_pct"].fillna(df["attendance_pct"].mean())
print(df.isna().sum())
# Subject Count Plot
sns.set_style("whitegrid")
fig ,ax = plt.subplots(figsize=(8,5))
df["fee_status"] = df["fee_status"].str.strip().str.lower()
sns.countplot(data=df,x="subject",hue="fee_status",order=df["subject"].value_counts().index,palette="Set2",edgecolor="black",linewidth=1.2,saturation=0.9, ax=ax)

for container in ax.containers:
    ax.bar_label(container,fontsize=9,padding=3)


ax.set_title("Number of Students per Subject(Count Plot)")
ax.set_xlabel("Subject")
ax.set_ylabel("Count")

plt.xticks(rotation=30)
ax.legend(title="Fee Status")

sns.despine()
# plt.savefig("Count_Plot.png")
plt.tight_layout()
plt.show()

# city count plot

sns.set_style("darkgrid")
fig,ax = plt.subplots(figsize=(9,5))
sns.countplot(data=df,x="city",
              hue="subject",
              order=df["city"].value_counts().index,
              palette="Set1",
              edgecolor="black",
              linewidth=1.4,
              saturation=1.0)

for container in ax.containers:
    ax.bar_label(container,fontsize=13,padding=3)

plt.xticks(rotation=30)
ax.legend(title="Subject")
ax.set_title("Number of Students per City(Count Plot)",fontsize=15,fontweight="bold")
sns.despine()
plt.tight_layout()
# plt.savefig("Count_Plot2.png")
plt.show()

