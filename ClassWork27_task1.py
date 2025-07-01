def print_words_reversed(filename):
    stack = []

    # Один проход по файлу: читаем слова и помещаем в стек
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            for word in line.strip().split():
                stack.append(word)

    # Печатаем в обратном порядке
    while stack:
        print(stack.pop(), end=' ')
