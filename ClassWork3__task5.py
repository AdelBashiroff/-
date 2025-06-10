def longest(strings):
    maximum = max(len(i) for i in strings)
    answer = [s for s in strings if len(s)==maximum]
    return answer
n = int(input())
spisok = []
for i in range(1, n+1):
    print("Добавьте слово в список")
    s = input()
    spisok.append(s)

result = longest(spisok)
print(result)