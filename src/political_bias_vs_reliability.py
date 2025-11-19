import json
import os
import matplotlib.pyplot as plt


scores = {
    "Washington Times": (33.46, 11.59),
    "TheWrap": (37.58, -5.98),
    "Fox News": (35.10, 11.09),
    "Reuters": (45.00, -1.32),
    "CBS News": (41.91, -3.02),
    "ABC News": (44.54, -3.13),
    "Boston Herald": (36.31, 9.68),
    "The New York Times": (40.97, -8.07),
    "USA Today": (40.91, -3.77),
    "Raw Story": (34.88, -13.62),
    "CNBC": (43.75, -1.95),
    "Washington Post": (38.71, -7.07),
    "MSNBC.com": (34.57, -13.86),
    "The Atlantic": (38.05, -9.34),
    "The New Yorker": (40.85, -12.48),
    "www.theepochtimes.com": (34.45, 8.14),
    "The Wall Street Journal": (43.32, 4.16),
    "Buzzfeed": (39.93, -6.05),
    "MSNBC": (34.57, -13.86)
}

with open(os.path.join("..", "data", "final_dataset.json"), "r", encoding="utf-8") as f:
    articles = json.load(f)


bias_values = []
reliability_values = []
labels = []

for article in articles:
    source = article.get("source", {}).get("name")
    if source in scores:
        reliability, bias = scores[source]
        bias_values.append(bias)
        reliability_values.append(reliability)
        labels.append(source)


plt.figure(figsize=(10, 7))
plt.scatter(bias_values, reliability_values)

for x, y, label in zip(bias_values, reliability_values, labels):
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(5, 5))

plt.axvline(0, color='black', linewidth=0.8)  # center bias line
plt.title("Reliability vs Political Bias of Newspaper Sources")
plt.xlabel("Political Bias (Left = Negative, Right = Positive)")
plt.ylabel("Reliability Score")

plt.grid(True, linestyle="--", alpha=0.5)


output_path = os.path.join("..", "data", "data_plot", "bias_vs_reliability.png")
plt.savefig(output_path, dpi=300)

print(f"Plot saved to {output_path}")