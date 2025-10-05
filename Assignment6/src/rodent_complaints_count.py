import argparse
import pandas as pd 
import os

def rodent_type_count(input_file, output_file):
    dt = pd.read_csv(input_file, parse_dates = ["Created Date", "Closed Date"])

    dt[dt["Complaint Type"].str.contains("Rodent", na = False) | 
        (dt["Complaint Type"].str.contains("Dead Animal", na = False)) & (dt["Descriptor"].str.contains("Rat or Mouse", na = False))]
    count = dt.groupby(["Location Type"]).size().reset_index(name = "Count")
    count.to_csv(output_file, index = False)

    exit()

rodent_type_count(os.path.join("..", "data", "311_2024.csv"), os.path.join("..", "data", "rodent_complaint_count.csv"))

## Is the following code correctly taking only the Complaint Type with "Rodent" and the Complaint Type "Dead Animal" with the descriptor "Rat or Mousse" and create a new csv file with the nomber of times each Location Type appears