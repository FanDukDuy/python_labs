import sys
from lib.text import normalize, tokenize, count_freq, top_n
tokens = tokenize(normalize(sys.stdin.read()))
freq = count_freq(tokens)
print("Всего слов:", len(tokens))
print("Уникальных слов:", len(freq))
print("Топ-5:")
for word, count in top_n(freq, 5):
    print(f"{word}:{count}")