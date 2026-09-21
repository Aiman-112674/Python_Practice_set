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

# KDE 

sns.set_style("whitegrid")
fig ,ax=plt.subplots(figsize=(9,5))
sns.kdeplot(data=df,x='marks',ax=ax,fill=True,color="steelblue")

ax.set_title("Distribution of Student Marks", fontsize=14,fontweight="bold")
ax.set_xlabel("Marks")
ax.set_ylabel("Density")


plt.tight_layout()
plt.show()

# Comparing Groups - real power of KDE :
fig,ax=plt.subplots(figsize=(8,5))
sns.kdeplot(data=df,x="marks",hue="fee_status",fill=True,alpha=0.4,common_norm=False,palette="Set1",linewidth=2,linestyle="--",bw_adjust=1,cut=0,clip=(0,100),log_scale=False,cumulative=False,ax=ax)

ax.set_title("Marks Distribution by Fee Status(KDE)",fontsize=16,fontweight="bold")
ax.set_xlabel("Marks",fontsize=12)
ax.set_ylabel("Density",fontsize=12)
ax.legend(title="Fee Status",labels=df["fee_status"].unique())
ax.axvline(df["marks"].mean(),color="red",linestyle="--",linewidth=1.5,label="Mean of Marks")
sns.despine()
plt.tight_layout()
plt.savefig("KDE Plot.png")
plt.show()

# Histogram + KDE Together 

fig,ax = plt.subplots(figsize=(8,5))
sns.histplot(data=df,x="marks",kde=True,ax=ax,color="skyblue",edgecolor="black")

ax.set_title("Marks Histogram With KDE Curve")
plt.tight_layout()
plt.show()

# Strip Plot

sns.set_style("dark")
fig ,ax = plt.subplots(figsize=(9,6))

sns.stripplot(data=df,x="subject",y="marks",ax=ax,color="steelblue",hue="fee_status",dodge=True,jitter=0.25,size=6,marker="o",alpha=0.6,palette="Set3",edgecolor="black",linewidth=0.5,order=df["subject"].value_counts().index)

ax.set_title("Marks Distribution per Subject (Strip Plot)", fontsize=14, fontweight='bold')
ax.set_xlabel("Subject",fontsize=12)
ax.set_ylabel("Marks",fontsize=12)
ax.legend(title="Fee Status")
ax.axhline(df["marks"].mean(),color="red",linestyle="--",linewidth=2,label="Mean")
plt.xticks(rotation=30)
sns.despine()
# plt.savefig("Strip Plot.png")
plt.tight_layout()
plt.show()

# Swarm Plot

sns.set_style("whitegrid")
fig,ax=plt.subplots(figsize=(10,6))

sns.swarmplot(
    data=df,
    x="subject",
    y="marks",
    hue="fee_status",
    dodge=True,
    size=6,
    marker="D",
    palette="Set3",
    edgecolor="black",
    linewidth=0.5,
    order=df["subject"].value_counts().index,
    ax=ax
)

ax.set_title("Marks Distribution per Subject (Swarm Plot, Split by Fee Status)", fontsize=14, fontweight='bold')
ax.set_xlabel("Subject", fontsize=12)
ax.set_ylabel("Marks", fontsize=12)
ax.legend(title="Fee Status")

ax.axhline(df["marks"].mean(),color="red",linestyle="--",linewidth=1.2,label="Mean")

plt.xticks(rotation=30)
sns.despine()
plt.tight_layout()
# plt.savefig("Swarm Plot.png")
plt.show()