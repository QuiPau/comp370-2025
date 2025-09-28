import sys 
import argparse 
import pandas as pd

def complaint_type_calculator(input_file, output_file):
    dt = pd.read_csv(input_file, usecols = ['Complaint Type', 'Borough'])
    counts = (
        dt.groupby(['Complaint Type', 'Borough']).size ().reset_index(name = 'count').sort_values(by = 'count', ascending = False)
    )
    counts.to_csv(output_file, index = False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", type = str, help = "Input file in CSV format")
    parser.add_argument("-s", type=str, help  = "Enter the start date")
    parser.add_argument("-e", type=str, help="Enter the end date")
    parser.add_argument("-o", type = str, help  = "Output file in CSV format")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    complaint_type_calculator(args.i,args.o)


if __name__ == "__main__":
    main()
