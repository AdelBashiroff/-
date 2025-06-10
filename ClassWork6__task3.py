def smoothness(string):
    maximum = max(len(s) for s in string)
    for i in range(len(string)):
        while len((string[i])) < maximum:
            string[i] += "*"
    return string

m = int(input())
spisok = []
for j in range(m):
    word = input()
    spisok.append(word)

result = smoothness(spisok)

print(result)