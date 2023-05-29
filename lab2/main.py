"""Подключение библиотеки numpy"""
import numpy as np
"""Ввод кол-ва строк, столбцов и номера строки. Проверка на ввод"""
try:
    print("Введите количество строк матрицы", end=" ")
    N = int(input())
except ValueError:
    print('Неверный ввод')
    exit()
try:
    print("Введите количество столбцов матрицы", end=" ")
    M = int(input())
except ValueError:
    print('Неверный ввод')
    exit()
try:
    print("Введите номер строки матрицы", end=" ")
    L = int(input())
except ValueError:
    print('Неверный ввод')
    exit()
"""Создание одномерного массива длиной равной кол-во строк умноженного на кол-во столбцов"""
a = np.array(range(N * M), int)
key = 0
s = []
"""Выбор метода заполнения массива, преобразование одномерного массива в двумерный, заполнение массива, проверка на 
ввод"""
while key != 1 and key != 2:
    key = int(input("Введите \"1\", если хотите выбрать ручной вывод, \"2\" -  для автоматической генерации: "))
    if key == 1:
        for i in range(N):
            b = str(i + 1)
            try:
                print("Введите " + b + " строку:")
                line = input()
                s = np.array(list(map(int, line.split())))
                a = a.reshape((N, M))
                a[i] = s
            except ValueError:
                print('Неверный ввод')
                exit()
    elif key == 2:
        a = np.random.randint(0, 9, size=(N, M))
    else:
        print("Неправильно выбран режим ввода")
        key = 0
"""Открытие текстового файла и запись в него исходного массива"""
file = open("otus.txt", "w+")
file.write("Исходная матрица: \n")
for i in range(N):
    for j in range(M):
        file.write(str(a[i, j]) + " ")
    file.write("\n")
arr = []
"""Запоминание нужной строки"""
for i in range(M):
    arr.append(a[L-1, i])
"""Прибавление выбранной строки ко всем строкам матрицы"""
for i in range(N):
    for j in range(M):
        a[i, j] = a[i, j] + arr[j]
"""Запись итоговой матрицы в текстовый файл"""
file.write("Итоговая матрица: \n")
for i in range(N):
    for j in range(M):
        file.write(str(a[i, j]) + " ")
    file.write("\n")
"""Закрытие текстового файла"""
file.close()
