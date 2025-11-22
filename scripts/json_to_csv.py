import json
import csv
import os
import re

def first_sentences(text, n=5):
    """
    Return the first n sentences of a text.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return " ".join(sentences[:n])


input_file = os.path.join("..", "data", "newsom_articles_filtered.json")
output_file = os.path.join("..", "data", "data_for_annotation_v2.csv")

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["title", "body", "sentiment", "source"])

    for item in data:
        title = item.get("title", "")
        body_full = item.get("body", "")
        body = first_sentences(body_full)
        sentiment = item.get("sentiment", "")

        source = item.get("source", {}).get("title", "")

        writer.writerow([title, body, sentiment, source])

print(f"CSV file '{output_file}' created successfully.")
