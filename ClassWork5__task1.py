def weather(string):
    coldest = max(string, key=lambda x: x[1])[0]
    wettest = min(string, key=lambda x: x[2])[0]
    return coldest, warmest

#пример данных
spisok = [
    (1, -5, 12), (2, -7, 10), (3, 0, 8), (4, 3, 4)
]
coldest, wettest = weather(spisok)
print(coldest, wettest)