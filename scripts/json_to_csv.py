import json
import csv
import os
import re

def first_sentence(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return " ".join(sentences[:4])

input_file = os.path.join("..","data", "final_dataset.json")
output_file = os.path.join("..", "data", "data_for_annotation.csv")

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    
    writer.writerow(["title", "body", "source"])
    
    for item in data:
        title = item.get("title", "")
        body_full = item.get("description", "")
        body = first_sentence(body_full)
        source = item.get("source", {}).get("name", "")
        
        writer.writerow([title, body, source])

print(f"CSV file '{output_file}' created successfully.")