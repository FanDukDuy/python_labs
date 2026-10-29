import csv
from pathlib import Path

from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """CSV -> XLSX: лист "Sheet1", первая строка — заголовок, ширина колонок по тексту (мин. 8)."""
    p = Path(csv_path)
    if p.suffix.lower() != ".csv":
        raise ValueError(f"Ожидался файл .csv: {csv_path}")
    if not p.exists():
        raise FileNotFoundError(csv_path)
    with p.open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        raise ValueError("CSV пуст")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in rows:
        ws.append(row)
    for col in ws.columns:
        width = max(len(str(c.value or "")) for c in col)
        ws.column_dimensions[col[0].column_letter].width = max(8, width)

    Path(xlsx_path).parent.mkdir(parents=True, exist_ok=True)
    wb.save(xlsx_path)