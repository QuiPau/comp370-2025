import sys
import argparse
import pandas as pd

def clean_data(input_file, output_file):
    df = pd.read_csv (input_file, parse_dates = ["Created Date", "Closed Date"], infer_datetime_format = True)
    cleaned_data = df[df["Created Date"] >= df["Closed Date"]] #Keep only lines with Created Date before Closed Date

    cleaned_data = cleaned_data.dropna(subset=["Closed Date", "Incident Zip"])
    
    cleaned_data.to_csv(output_file, index = False)


def main ():
    parser= argparse.ArgumentParser()
    parser.add_argument("-i", type = str, help = "Input file", required = True)
    parser.add_argument("-o", type = str, help = "Output file", required = True)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    clean_data(args.i, args.o)

if __name__ == "__main__" :
    main()