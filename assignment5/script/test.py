import requests
import pandas as pd

url = "https://data.cityofnewyork.us/resource/jrb2-thup.json"

limit = 1000
offset = 0
first_chunk = True

while True:
    response = requests.get(url, params={"$limit": limit, "$offset": offset}, timeout=10)
    response.raise_for_status()  # will raise an error if request fails

    data = response.json()
    if not data:
        break

    df = pd.DataFrame(data)
    df.to_csv(
        "/home/pquidu/repo/comp370-2025/assignment5/data/NYU_data.csv",
        mode='w' if first_chunk else 'a',
        header=first_chunk,
        index=False,
        encoding='utf-8'
    )

    first_chunk = False
    offset += limit~
    print(f"Fetched {offset} rows...")

data=[]

""" response = requests.get(url)                #https://stackoverflow.com/questions/60191014/valueerror-invalid-file-path-or-buffer-object-type-class-dict-python
content = json.loads(response.text)
data = pd.DataFrame(content)
print (type(data))
print(len(data)) """