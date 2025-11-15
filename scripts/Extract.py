import requests
import json

url = "https://api.thenewsapi.com/v1/news/all"
params = {
    "api_token": "pjGb3ffAdiAQotIbjcGXPY08zgWyqPOxnTtasOKM",
    "search": "Gavin Newsom",
    "published_after": "2024-11",
    "published_before": "2025-11",
    "limit": 50,
}

response = requests.get(url, params=params)

data = response.json()

with open("test.json", "w") as file:
    json.dump(data, file)

print(response.json())
