import json
from collections import Counter
import os
import matplotlib.pyplot as plt

# Load your JSON file
with open(os.path.join("..", "data", "final_dataset.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract newspaper titles
newspapers = [article["source"]["name"] for article in data if "source" in article]

# Count unique newspapers
distribution = Counter(newspapers)

# Display the distribution
print("Distribution of Newspapers:")
for newspaper, count in distribution.items():
    print(f"{newspaper}: {count}")

print("\nNumber of unique newspapers:", len(distribution))

# ---- Political leaning classification ---- #

left_sources = {
    "MSNBC.com", "MSNBC",
    "The Atlantic",
    "nytimes.com", "The New York Times",
    "The New Yorker",
    "Washington Post",
    "HuffPost", "Raw Story",
    "TheWrap",
    "Buzzfeed"
}

centrist_sources = {
    "CBS News", "CNBC",
    "ABC News",
    "Reuters",
    "USA Today"
}

right_sources = {
    "Fox News",
    "Washington Times",
    "The Wall Street Journal",
    "New York Post",
    "Boston Herald",
    "The Epoch Times"
}


# Count totals for each category
left_count = sum(distribution.get(src, 0) for src in left_sources)
centrist_count = sum(distribution.get(src, 0) for src in centrist_sources)
right_count = sum(distribution.get(src, 0) for src in right_sources)

# ---- Pie chart ---- #
labels = ["Left", "Centrist", "Right"]
sizes = [left_count, centrist_count, right_count]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Political Leaning Distribution of Newspapers")
plt.show()
