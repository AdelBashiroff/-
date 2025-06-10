#1
import re

pattern = r'[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Пример:
text = "Мой адрес example@mail.ru, а у друга — user42@gmail.com"
emails = re.findall(pattern, text)
print(emails)

#2
import re
def extract_phone_numbers(input_file, output_file):
    # Регулярное выражение для поиска номеров
    pattern = r"\+7-\d{3}-\d{3}-\d{2}-\d{2}"

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Нахожу все номера
    phone_numbers = re.findall(pattern, text)

    # Сохранить в новый файл
    with open(output_file, 'w', encoding='utf-8') as f:
        for number in phone_numbers:
            f.write(number + '\n')

# Пример
extract_phone_numbers('input.txt', 'phones.txt')

#3
import re

text = "Сегодня 11.06.2025, а завтра будет 12.06.2025. Ошибочные даты: 32.01.2024, 15.13.2023."

pattern = r"\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}\b"

dates = re.findall(pattern, text)

print(dates)

#4
import re

text = "Сегодня отличный День для прогулки в Central Park и на улице Красная."

pattern = r"\b[A-ZА-ЯЁ][a-zа-яё]*\b"

matches = re.findall(pattern, text, re.IGNORECASE | re.UNICODE)
print(matches)

#5
import re
def is_only_digits(s):
    return bool(re.fullmatch(r"^\d+$", s))

print(is_only_digits("12345"))   #True
print(is_only_digits("123a45"))  #False
print(is_only_digits(""))        #False


