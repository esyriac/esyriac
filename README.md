A script to convert a parquet file to a CSV or Excel for easy filtering and further data processing. 

This is a python script that takes a parquet file as input and generates either a CSV or Excel file after conversion. 

This is written in python using pandas API.

It needs a Python environent to run the script and below packages should be installed - 
# pip install pandas
# pip install pyarrow
# pip install xlsxwriter

Command usage - python convert-parquet.py <source-filename> <output-format>
The output-format is optional and default output is csv.

if the paramters are not passed as argument, the program will ask to provide at execution time. The output will be saved in the same folder with the same filename as the source with the appropriate file type.

