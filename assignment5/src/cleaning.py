import pandas as pd
import os

data_path = os.path.join("..", "data", "nyc_311_2024.csv")

dt = pd.read_csv(data_path, parse_dates=['Created Date', 'Closed Date'])

dt = dt[dt["Created Date"] <= dt['Closed Date']]
dt = dt.dropna(subset=["Incident Zip", 'Closed Date'])

dt.to_csv(os.path.join("..", "data", "cleaned_data.csv"), index = False)