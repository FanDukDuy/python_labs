import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает файл целиком и возвращает содержимое одной строкой.

    Другая кодировка выбирается параметром encoding, например:
    read_text("data/input.txt", encoding="cp1251").

    FileNotFoundError (файла нет) и UnicodeDecodeError (кодировка
    не подходит) не перехватываются, пусть падают.
    """
    return Path(path).read_text(encoding=encoding)


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Создаёт или перезаписывает CSV-файл с разделителем ','.

    Если передан header, он записывается первой строкой.
    Если строки в rows разной длины, поднимается ValueError.
    """
    rows = list(rows)
    if len({len(r) for r in rows}) > 1:
        raise ValueError("Строки в rows имеют разную длину")

    with Path(path).open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        w.writerows(rows)

