import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    '''Преобразует JSON (список словарей) в CSV.'''
    if Path(json_path).suffix != ".json" or Path(csv_path).suffix != ".csv":
        raise ValueError("Неверный формат файла")

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list) or not data or not all(isinstance(x, dict) for x in data):
        raise ValueError("Некорректный JSON")

    fields = list(dict.fromkeys(key for item in data for key in item))

    if not fields:
        raise ValueError("В JSON нет полей")

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    '''Преобразует CSV в JSON (список словарей).'''
    if Path(csv_path).suffix != ".csv" or Path(json_path).suffix != ".json":
        raise ValueError("Неверный формат файла")

    with open(csv_path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        if not reader.fieldnames:
            raise ValueError("CSV пуст")

        data = list(reader)

    if not data:
        raise ValueError("CSV не содержит записей")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
