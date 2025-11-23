# 📘 Reel Engagement Time Visualizer

This project helps identify the **best time to upload a reel** on social media using engagement data stored in a CSV file.  
The script reads the dataset, asks the user for a day, and plots a **simple line chart** showing engagement for every time interval.

---

## 📂 Files Included
- **reel_engagement_data.csv** — Engagement data for each 15-minute interval  
- **visualizer.py** — The Python script (main code)

---

## 🧠 What the Script Does
- Loads reel engagement data from a CSV  
- Asks the user to enter a day (e.g., `monday`, `tuesday`, etc.)  
- Validates the input  
- Plots engagement values for that day  
- Helps find the best time of the day to upload a reel

---

## 🛠️ Requirements
Install the necessary Python libraries:

```bash
pip install pandas matplotlib
