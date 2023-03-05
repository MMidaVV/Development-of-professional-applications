arr = []
minimum = 10000000
n = int(input("Введите количество элементов: "))
for i in range(n):
    a = str(i + 1)
    print("Введите элемент массива " + a, end=" ")
    arr.append(int(input()))
    if arr[-1] < minimum:
        minimum = arr[-1]
print(f"Минимальный элемент массива: {minimum}")
