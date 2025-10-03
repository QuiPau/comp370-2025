import pandas as pd 
import os
import sys
import argparse

def complaint_type_generator(input_file, output_file, starting_date, ending_date):
    dt = pd.read_csv(input_file, parse_dates = ['Created Date', 'Closed Date'])
    start = pd.to_datetime(starting_date)
    end = pd.to_datetime(ending_date)
    dt = dt[(dt["Created Date"] >= start) & (dt['Closed Date'] <= end)]
    count = dt.groupby(["Complaint Type", "Borough"]).size().sort_values(ascending=False).reset_index(name = "Count")
    print(count.head())
    count.to_csv(output_file, index = False)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", type = str, help = "input csv file")
    parser.add_argument("-s", type = str, help = "starting date")
    parser.add_argument("-e", type = str, help = "ending date")
    parser.add_argument("-o", type = str, help = "output file")

    if len(sys.argv != 4):
        parser.print(sys.stderr)
        exit(1)


    args = parser.parse_args()

    complaint_type_generator(args.i, args.o, args.s, args.e)




if __name__ == "__main__": 
    main()

