import csv
from pathlib import Path
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    '''Конвертирует CSV в XLSX: лист Sheet1, автоширина колонок.'''
    if Path(csv_path).suffix != ".csv" or Path(xlsx_path).suffix != ".xlsx":
        raise ValueError("Неверный формат файла")

    with open(csv_path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))

    if not rows:
        raise ValueError("CSV пуст")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    for col in ws.columns:
        width = max(len(str(cell.value or "")) for cell in col)
        ws.column_dim[col[0].column_letter].width = max(8, width)

    wb.save(xlsx_path)