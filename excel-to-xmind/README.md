# Excel to XMind Converter

This project provides a tool to convert Excel content into XMind mind map format. It is designed to help users easily visualize data from Excel spreadsheets in a mind map format.

## Project Structure

```
excel-to-xmind
├── src
│   ├── main.py          # Entry point of the program
│   ├── converter.py     # Contains the ExcelToXMindConverter class
│   ├── utils.py         # Utility functions for reading Excel and writing XMind
│   └── types
│       └── __init__.py  # Type definitions for Excel rows and XMind nodes
├── requirements.txt     # Required Python libraries
└── README.md            # Project documentation
```

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

1. Prepare your Excel file with the necessary data.
2. Run the main program:

```
python src/main.py <path_to_your_excel_file>
```

3. The program will generate an XMind file based on the content of the Excel file.

## Example

Assuming you have an Excel file named `data.xlsx`, you can convert it to XMind format by executing:

```
python src/main.py data.xlsx
```

This will create an XMind file in the same directory as your Excel file.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.