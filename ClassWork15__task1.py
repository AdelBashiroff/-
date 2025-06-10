def count_lines_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print("Файл не найден.")
        return 0

filename = 'example.txt'
line_count = count_lines_in_file(filename)
print("Количество строк в файле:", line_count)