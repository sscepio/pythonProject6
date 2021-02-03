# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Задание 1
a = input("Введите число - a ")
b = input("Введите число - b ")
name = input("Введите Ваше имя - ")
print(int(a) + int(b))
print(name)
# Задание 2
N = int(input("Введите секунды "))
min = 60
hour = 60 * 60
day = 60 * 60 * 24
HOUR = N // hour
MINUT = (N - (HOUR * hour)) // min
SECONDS = N - ((HOUR * hour) + (MINUT * min))
print('{}:{}:{}'.format(HOUR, MINUT, SECONDS))


# Задание 3
c = input("Введите число - c ")
print(int(c) + int(c+c) + int(c+c+c))

# Задание 4
n = input("Введите число - ")
i = int(n)
r = -1
while i > 10:
    d = i % 10
    i //= 10
    if d > r:
        r = d
print(r)
# Задание 5
q = input("Введите выручку ")
cost = input("Введите издержки ")
e = input("Введите количество сотрудников ")
if int(q) - int(cost) > 0:
    print("Прибыль — выручка больше издержек")
    print(f"Соотношение прибыли к выручке {(int(q) - int(cost))/int(q)}")
    print(f"Соотношение прибыли на 1 сотрудника {(int(q) - int(cost)) / int(e)}")
else:
    print("убыток — издержки больше выручки")
# Задание 6
a = int(input("Введите a - "))
b = int(input("Введите b - "))
z = 1
while a < b:
    a *= 1.1
    z += 1
print(f"на {z} день спортсмен достиг результата — не менее {b} км.")