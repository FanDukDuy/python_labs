import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Приводит текст к единому виду: регистр, ё→е, пробелы."""
    text = text.casefold() if casefold else text.lower()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    """Разбивает текст на слова (буквы, цифры, дефис внутри слова)."""
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Считает, сколько раз встретилось каждое слово."""
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Топ-N слов: по убыванию частоты, при равенстве по алфавиту."""
    return sorted(freq.items(), key=lambda p: (-p[1], p[0]))[:n]

# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"
assert normalize("Hello\r\nWorld") == "hello world"
assert normalize("  двойные    пробелы  ") == "двойные пробелы"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("hello,world!!!") == ["hello", "world"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]
assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

# count_freq + top_n
freq = count_freq(["a", "b", "a", "c", "b", "a"])
assert freq == {"a": 3, "b": 2, "c": 1}
assert top_n(freq, 2) == [("a", 3), ("b", 2)]

# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]

print("Все тесты пройдены")