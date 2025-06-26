print("Welcome to the Excel to XMind converter!")

import pandas as pd
from converter import ExcelToXMindConverter
from utils import read_excel, write_xmind

def main():
    # Specify the path to the Excel file and the output XMind file
    excel_file_path = 'path/to/your/excel/file.xlsx'
    xmind_file_path = 'path/to/your/output/file.xmind'
    
    # Read the Excel data
    excel_data = read_excel(excel_file_path)
    
    # Create an instance of the converter
    converter = ExcelToXMindConverter()
    
    # Convert the Excel data to XMind format
    xmind_data = converter.convert(excel_data)
    
    # Write the XMind data to a file
    write_xmind(xmind_data, xmind_file_path)
    
    print("Conversion completed! XMind file created at:", xmind_file_path)

if __name__ == "__main__":
    main()