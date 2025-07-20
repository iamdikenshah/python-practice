news_key="News api key"

import requests
import json
import os

base_url = "https://newsapi.org/v2/"



query = input("What are you interested on??\n")
from_date = "2025-06-20"
sort_by = "publishedAt"

url = f"{base_url}everything?q={query}&from={from_date}&sortBy={sort_by}&apiKey={news_key}"

print(f"Fetching news from: {url}"  )
request = requests.get(url)
print(f"Status code: {request.status_code}")  # Should print 200 if the request was successful
# print(request.json())  # Print the JSON response from the API 

match request.status_code:
    case 200:
        articals = request.json().get('articles')
        for artical in articals:
            print(f"Title: {artical.get("title")}\n")
