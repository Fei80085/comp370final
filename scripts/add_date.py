import csv
import json
import os

# --- FILE PATHS (update these to your actual files) ---
CSV_INPUT = os.path.join("..", "data", "data_annotated.csv")
JSON_INPUT = os.path.join("..", "data", "newsom_articles_filtered.json")
CSV_OUTPUT = "articles_with_dates.csv"

with open(JSON_INPUT, "r", encoding="utf-8") as f:
    json_data = json.load(f)

title_to_date = {}
for entry in json_data:
    title = entry.get("title", "").strip()
    date = entry.get("date", "missing")
    title_to_date[title] = date

with open(CSV_INPUT, "r", encoding="utf-8") as infile, \
     open(CSV_OUTPUT, "w", encoding="utf-8", newline="") as outfile:
    
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["date"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        csv_title = row["title"].strip()
        
        # Lookup date from JSON
        row["date"] = title_to_date.get(csv_title, "missing")
        
        writer.writerow(row)

print("Done! Output written to:", CSV_OUTPUT)
