import re


def stat(list):
    dicList = []
    dicSet = []

    for i in list:
        if dicList.count(i) == 0:
            dicList.append(i)
            dicSet.append([i, list.count(i)])

    return dicSet


def P(x): return int(x)


def S(s): return s[1]


txt = (open("text.txt", "r", encoding="utf-8")).read()

digits = re.findall(r"\d", txt)
numbers = re.findall(r"\d+", txt)
digits.sort(key=P)
numbers.sort(key=P)

DigStat = stat(digits)
NumStat = stat(numbers)
DigStat.sort(key=S, reverse=True)
NumStat.sort(key=S, reverse=True)

print(f'Цифры: {digits}\nЧисла: {numbers}\n\nСтатистика цифр: {DigStat}\nСтатистика чисел: {NumStat}')
