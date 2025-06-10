#1
# Ввод списка строк
words = ["apple", "banana", "avocado", "blueberry", "cherry"]

# Инициализация пустого словаря
grouped_words = {}

# Перебираем все слова в списке
for word in words:
    first_letter = word[0].lower()  # Получаем первую букву независимо от регистра

    # Если буква уже есть в словаре, добавляем слово в список
    if first_letter in grouped_words:
        grouped_words[first_letter].append(word)
    else:
        # Если буквы нет в словаре, создаём новый список с этим словом
        grouped_words[first_letter] = [word]

# Выводим результат
print(grouped_words)

#2
# Ввод списка строк
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Инициализация пустого словаря
anagrams = {}

# Перебираем все слова в списке
for word in words:
    # Сортируем символы в слове и превращаем их в строку
    sorted_word = ''.join(sorted(word))

    # Если отсортированное слово уже есть в словаре, добавляем текущее слово
    if sorted_word in anagrams:
        anagrams[sorted_word].append(word)
    else:
        # Если отсортированного слова нет в словаре, создаем новый список
        anagrams[sorted_word] = [word]

# Выводим результат
print(anagrams)

#3
# Ввод строки
text = "This is a simple test"

# Разбиваем строку на слова
words = text.split()

# Инициализация пустого словаря
word_lengths = {}

# Перебираем все слова
for word in words:
    length = len(word)  # Определяем длину слова

    # Если длина уже есть в словаре, добавляем слово в соответствующий список
    if length in word_lengths:
        word_lengths[length].append(word)
    else:
        # Если длины нет в словаре, создаем новый список
        word_lengths[length] = [word]

# Выводим результат
print(word_lengths)

#4
import itertools

# Ввод списков
list1 = [1, 2]
list2 = ['a', 'b']

# Получение декартова произведения
result = list(itertools.product(list1, list2))

# Вывод результата
print(result)

#5
# Ввод списка строк
words = ["word", "rev"]

# Преобразуем каждое слово в палиндром
palindromes = [word + word[:-1][::-1] for word in words]

# Выводим результат
print(palindromes)

#6
from collections import Counter

# Ввод строки
input_string = "success"

# Подсчитываем количество каждого символа
count = Counter(input_string)

# Строим уникальный идентификатор
unique_identifier = ""
for char in input_string:
    # Если символ ещё не был добавлен в результат
    if char not in unique_identifier:
        # Проверяем количество вхождений символа
        if count[char] % 2 == 0:
            # Если чётное количество, добавляем символ в нижнем регистре
            unique_identifier += char.lower()
        else:
            # Если нечётное количество, добавляем символ в верхнем регистре
            unique_identifier += char.upper()

# Выводим результат
print(unique_identifier)

#7
# Словарь синонимов
synonyms = {'quick': 'fast', 'brown': 'dark'}

# Ввод текста
input_text = "quick brown fox"

# Разбиваем текст на слова
words = input_text.split()

# Заменяем слова на синонимы
modified_words = [synonyms.get(word, word) for word in words]

# Собираем текст обратно
output_text = " ".join(modified_words)

# Выводим результат
print(output_text)
