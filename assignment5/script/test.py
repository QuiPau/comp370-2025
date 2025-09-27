import requests
import pandas as pd

url = "https://data.cityofnewyork.us/resource/jrb2-thup.json"
response = requests.get(url)

if response.status_code == 200:
    print("Success!")
    data = response.json()
    df = pd.DataFrame(data)  # create DataFrame directly from JSON
    df.to_csv('~/repo/comp370-2025/assignment5/data/NYU_dataset.csv', encoding='utf-8', index=False)
else:
    print(f"Request failed with status code {response.status_code}")