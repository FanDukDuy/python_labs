import argparse, sys
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

CMDS = {"json2csv": json_to_csv, "csv2json": csv_to_json, "csv2xlsx": csv_to_xlsx}

def main():
    p = argparse.ArgumentParser(description="Конвертеры JSON/CSV/XLSX")
    sub = p.add_subparsers(dest="command", required=True)
    for name in CMDS:
        sp = sub.add_parser(name, help=name)
        sp.add_argument("--in", dest="src", required=True)
        sp.add_argument("--out", dest="dst", required=True)

    a = p.parse_args()
    try:
        CMDS[a.command](a.src, a.dst)
    except (FileNotFoundError, ValueError) as e:
        print(f"ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()