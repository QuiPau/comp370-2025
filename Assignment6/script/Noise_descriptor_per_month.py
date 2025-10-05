import pandas as pd
import matplotlib.pyplot as plt 
import os

df = pd.read_csv(os.path.join("..", "data", "descriptor_for_each_month.csv"))
df["TotalPerMonth"] = df.groupby("Month")["Count"].transform("sum")
df["Percentage"] = (df["Count"] / df["TotalPerMonth"]) * 100


pivot = df.pivot(index="Month", columns="Descriptor", values="Percentage").fillna(0)

""" pivot.plot(kind="bar", stacked=True, figsize=(12,6))
plt.ylabel("Percentage of Complaints (%)")
plt.title("Noise Complaint Descriptor Distribution per Month")
plt.legend(title="Descriptor", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout() """

pivot.plot.area(figsize=(12,6), alpha=0.7)
plt.ylabel("Percentage of Complaints (%)")
plt.title("Noise Complaint Descriptor Distribution per Month")
plt.legend(title="Descriptor", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(range(1,13))
plt.tight_layout()
plt.savefig(os.path.join("..", 'plots', 'task1_plot.png'))
