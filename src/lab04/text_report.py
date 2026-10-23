import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1])) 
from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv

try:
    text = read_text("data/input.txt")
except FileNotFoundError:
    sys.exit("Ошибка: файл data/input.txt не найден")

tokens = tokenize(normalize(text))
freq = count_freq(tokens)

write_csv(top_n(freq, len(freq)), "data/report.csv", header=("word", "count"))

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")
for word, count in top_n(freq, 5):
        print(f"{word}:{count}")


