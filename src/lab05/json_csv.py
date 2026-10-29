import csv
import json
from pathlib import Path


def _open_checked(path: str, suffix: str):
    p = Path(path)
    if p.suffix.lower() != suffix:
        raise ValueError(f"Ожидался файл {suffix}: {path}")
    if not p.exists():
        raise FileNotFoundError(path)
    return p.open(encoding="utf-8", newline="")


def json_to_csv(json_path: str, csv_path: str) -> None:
    """JSON (список словарей) -> CSV. Колонки как в первом объекте, пропуски — ''."""
    with _open_checked(json_path, ".json") as f:
        data = json.load(f)  # пустой/битый JSON -> JSONDecodeError (это ValueError)
    if not isinstance(data, list) or not data or not all(isinstance(d, dict) for d in data):
        raise ValueError("JSON должен быть непустым списком словарей")
    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(data[0]), restval="", extrasaction="ignore")
        w.writeheader()
        w.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """CSV (с заголовком) -> JSON (список словарей), значения — строки."""
    with _open_checked(csv_path, ".csv") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError("CSV пуст или нет данных под заголовком")
    Path(json_path).parent.mkdir(parents=True, exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)