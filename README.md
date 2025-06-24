# pytools

This repository contains small utility scripts written in Python.

## Excel Example

`test.py` offers a minimal command-line interface for manipulating Excel files
using the `openpyxl` library. Install the dependency and run the script as
follows:

```bash
pip install openpyxl
python test.py list                # list rows in the default workbook
python test.py add Alice 30        # append a row to the workbook
```

The workbook defaults to `example.xlsx`. Specify an alternate path with
`--file <path>` if needed.
