"""Simple Excel manipulation script using openpyxl.

This script demonstrates how to create an Excel file, append a row,
and print existing rows. It requires the ``openpyxl`` package. If the
package is missing, the script prints an instruction message and exits.
"""

import os
import sys

try:
    from openpyxl import Workbook, load_workbook
except ImportError:
    print("openpyxl is required. Install it with 'pip install openpyxl'.")
    sys.exit(0)

FILENAME = "example.xlsx"


def create_workbook(path: str) -> None:
    """Create a workbook with a header row."""
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"
    ws.append(["Name", "Age"])
    wb.save(path)


def append_row(path: str, name: str, age: int) -> None:
    """Append a row of data to the workbook."""
    if not os.path.exists(path):
        create_workbook(path)
    wb = load_workbook(path)
    ws = wb.active
    ws.append([name, age])
    wb.save(path)


def print_rows(path: str) -> None:
    """Print all rows in the workbook."""
    if not os.path.exists(path):
        print(f"No workbook found at {path}.")
        return
    wb = load_workbook(path)
    ws = wb.active
    for row in ws.iter_rows(values_only=True):
        print("\t".join(str(cell) for cell in row))


def main() -> None:
    append_row(FILENAME, "Alice", 30)
    append_row(FILENAME, "Bob", 25)
    print("Current contents of the workbook:")
    print_rows(FILENAME)


if __name__ == "__main__":
    main()
