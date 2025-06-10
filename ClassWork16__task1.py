import re

strings = [
    "Привет",
    "Это строка с числом 123",
    "Без цифр",
    "42 — ответ",
    "abc",
    "0 в начале",
    "три5пять"
]

pattern = r".*\d.*"

for s in strings:
    if re.match(pattern, s):
        print(f"'{s}' содержит хотя бы одну цифру")
    else:
        print(f"'{s}' не содержит цифр")