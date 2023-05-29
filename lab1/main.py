"""Подключение библиотеки рандомных чисел"""
import random

"""Получение количества элементов"""
try:
    n = int(input("Введите количество элементов: "))
except ValueError:
    print('Неверный ввод')
    exit()
"""Получение ключа выбора метода программы"""
try:
    metod = int(input("Введите \"1\", если хотите выбрать метод стандартных функций,"
                      " \"2\" -  если хотите выбрать метод без стандартных функций: "))
except ValueError:
    print('Неверный ввод')
    exit()


def func1():
    arr = []
    key = '0'
    """Получение ключа метода ввода, проверка ключа ввода элементов, получение элементов, и проверка правильности ввода
        ключа"""
    while key != '1' and key != '2':
        key = input("Введите \"1\", если хотите выбрать ручной вывод, \"2\" -  для автоматической генерации: ")
        if key == "1":
            for i in range(n):
                a = str(i + 1)
                print("Введите элемент массива " + a, end=" ")
                arr.append(int(input()))
        elif key == '2':
            arr = [random.randint(0, 15) for i in range(n)]
        else:
            print("Неправильно выбран режим ввода")
            key = 0
    """Вывод исходного массива"""
    print("Исходный массив массив :")
    for i in range(n):
        print(arr[i], end=" ")
    """Нахождение максимального элемента"""
    maxi = max(arr)
    print("\nМаксимальный элемент:\n" + str(maxi))
    """Нахождение и удаление чётных элементов"""
    arr1 = []
    check = 0
    i = 0
    while i < n:
        if arr[i] == maxi:
            check = 1
        if check == 0:
            arr1.append(arr[i])
            i += 1
        elif check != 0:
            if arr[i] % 2 == 0:
                i += 1
            else:
                arr1.append(arr[i])
                i += 1
    """Вывод итогового массива"""
    print("Итоговый массив массив :")
    for i in range(len(arr1)):
        print(arr1[i], end=" ")


def func():
    arr = []
    key = '0'
    """Получение ключа метода ввода, проверка ключа ввода элементов, получение элементов, и проверка правильности ввода 
    ключа"""
    while key != '1' and key != '2':
        key = input("Введите \"1\", если хотите выбрать ручной вывод, \"2\" -  для автоматической генерации: ")
        if key == "1":
            for i in range(n):
                a = str(i + 1)
                print("Введите элемент массива " + a, end=" ")
                arr.append(int(input()))
        elif key == '2':
            arr = [random.randint(0, 15) for i in range(n)]
        else:
            print("Неправильно выбран режим ввода")
            key = 0
    max = -11111
    """Вывод исходного массива"""
    print("Исходный массив :")
    for i in range(n):
        print(arr[i], end=" ")
    """Нахождение максимального элемента"""
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
            maxi = i
    print("\nМаксимальный элемент:\n" + str(max))
    """Нахождение и удаление чётных элементов, нахождение кол-ва элементов итогового списка"""
    maxi = maxi + 1
    arr1 = []
    k = maxi
    for i in range(maxi):
        arr1.append(arr[i])
    while maxi < n:
        if arr[maxi] % 2 == 0:
            maxi += 1
        else:
            arr1.append(arr[maxi])
            k += 1
            maxi += 1
    """Вывод итогового массива"""
    print("Итоговый массив массив :")
    for i in range(k):
        print(arr1[i], end=" ")


"""Вызов основной части программы в зависимости от ключа метода программы"""
if metod == 2:
    func()
elif metod == 1:
    func1()
