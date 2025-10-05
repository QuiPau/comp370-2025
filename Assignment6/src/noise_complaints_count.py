import pandas as pd
import argparse

#Csv file to display the count of each unique Descriptor per month

def noise_type_count(input_file, output_file):
    dt = pd.read_csv(input_file, parse_dates=['Created Date', 'Closed Date'])
    noise = dt[dt["Complaint Type"].str.startswith("Noise - ", na = False)].copy()
    noise["Month"] = noise["Created Date"].dt.month 
    count = noise.groupby(["Descriptor", "Month"]).size().reset_index(name = "Count")

    count.to_csv(output_file, index = False)



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", type = str, help = "input file")
    parser.add_argument("-o", type = str, help = "output file")

    args = parser.parse_args()

    noise_type_count(args.i, args.o)



if __name__ == "__main__":
    main()