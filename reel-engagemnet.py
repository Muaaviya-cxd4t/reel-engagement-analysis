import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("reel_engagement_data.csv")
day = input("Enter the day you want to upload : ").lower() 
if day not in df.columns:
    print("Invalid day!")
    exit()
plt.figure(figsize=(12,6))
plt.plot(df["Time Interval"], df[day])
plt.xticks(rotation=90, fontsize=8)
plt.title(f"Best Reel Upload Time on {day}")
plt.xlabel("Time Interval")
plt.ylabel("Engagement")
plt.show()
