import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(os.path.join("..", "data", "first_10_rodent_location.csv"))
print(df.head())

keep_categories = ["Street/Sidewalk", "Residential Building/House", "Store/Commercial"]

df["Location Grouped"] = df["Location Type"].apply(
    lambda x: x if x in keep_categories else "Other"
)

grouped = df.groupby("Location Grouped", as_index=False)["Count"].sum()

total_count = grouped["Count"].sum()
grouped["Percentage"] = (grouped["Count"] / total_count) * 100

print(grouped)

plt.figure(figsize=(8, 6))
plt.pie(
    grouped["Percentage"], 
    labels=grouped["Location Grouped"], 
    autopct="%.1f%%", 
    startangle=90
)
plt.title("Rodent Sightings by Location Type")
plt.savefig(os.path.join("..", 'plots', 'task2_plot.png'))
