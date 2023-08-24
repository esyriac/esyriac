import pandas as pd
import pyarrow.parquet as py
import os
import sys


#install these packages
# pip install pandas
# pip install pyarrow
# pip install xlsxwriter


def parquet_to_csv(parquet_file, csv_file):
    try:
        # Read the Parquet file
        table = py.read_table(parquet_file)

        # Convert the Parquet table to a DataFrame
        df = table.to_pandas()

        # Write the DataFrame to a CSV file
        df.to_csv(csv_file, index=False)
        
        print(f"Conversion complete. Parquet file '{parquet_file}' converted to CSV file '{csv_file}'.")
    except Exception as e:
        print(f"An error occurred while Processing: {str(e)}")

def parquet_to_excel(parquet_file, excel_file):
    try:
        # Read the Parquet file
        table = py.read_table(parquet_file)

        # Convert the Parquet table to a DataFrame
        df = table.to_pandas()

        # Write the DataFrame to a Excel file
        writer = pd.ExcelWriter(excel_file, engine='xlsxwriter') 
        df.to_excel(excel_file)

        print(f"Conversion complete. Parquet file '{parquet_file}' converted to Excel format file '{excel_file}'.")
    except Exception as e:
        print(f"An error occurred while processing : {str(e)}")


if __name__ == "__main__":
    # Specify the input Parquet file and output format file
    #print (f" Input value count : {len(sys.argv)} ")
    input_parquet_file = None
    output_format = None

    if len(sys.argv) >= 2 :
        input_parquet_file = sys.argv[1] 

    if len(sys.argv) >= 3 :     
        output_format = sys.argv[2] 
    
    if input_parquet_file is None: 
        input_parquet_file  = input("Enter the name of the file to convert : ")    
  
    if ".parquet" not in input_parquet_file :
        input_parquet_file = input_parquet_file + ".parquet"

    if output_format is None:
        output_format  = input("Enter the output format, options are csv or xls and default is csv : ")    

    #print (f" Output foramt  : {output_format} ")
    if output_format is None or output_format == "" :
        output_format = "csv"

    filename_without_extension, _ = os.path.splitext(input_parquet_file)
    
    if output_format == "csv" :
        output_file = filename_without_extension + ".csv"
        print(f"Initiating conversion to CSV format...") 
        parquet_to_csv(input_parquet_file, output_file)
    elif output_format == "xls" :
        output_file = filename_without_extension + ".xlsx"
        print(f"Initiating conversion to Excel format...") 
        parquet_to_excel(input_parquet_file, output_file)    
    else :
        print(f"Invalid output type identified. Existing")    

