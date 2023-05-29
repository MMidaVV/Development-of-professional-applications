import os
import csv


def printlist(mylist):
    for x in mylist:
        print(x)


def sort_cost(mylist, sign, quantity):
    for x in mylist:
        if sign == '>':
            if int(x["Likes"]) > quantity:
                print(x)
        elif sign == '<':
            if int(x["Likes"]) < quantity:
                print(x)
        elif sign == '!=':
            if x["Likes"] != quantity:
                print(x)
        elif sign == '>=':
            if int(x["Likes"]) >= quantity:
                print(x)
        elif sign == '<=':
            if int(x["Likes"]) <= quantity:
                print(x)
        elif sign == '==':
            if x["Likes"] == quantity:
                print(x)


def sort_name(mylist):
    print("Сортировка по названию(по убыванию):")
    mylist.sort(key=lambda x: x['Name'])
    printlist(mylist)


def sort_like(mylist):
    print("Сортировка по стоимости(по убыванию):")
    mylist.sort(key=lambda x: int(x['Likes']))
    new_list = list(reversed(mylist))
    printlist(new_list)


if __name__ == '__main__':
    print("Количество файлов в директории:", len(os.listdir(path=".")))
    mylist = {}
    with open("data.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=";")
        mylist = [row for row in reader]
    key = int(
        input("Введите \n1 - если хотите увидеть сортировку файла по именам в алфавитном порядке, \n2 - если хотите "
              "увидеть сортировку по лайкам по возрастанию, \n3 - если хотите увидеть только строки с определённым "
              "количеством лайков, \n4 - если просто хотите вывести все строки\n")
    )
    if key == 1:
        sort_name(mylist)
    elif key == 2:
        sort_like(mylist)
    elif key == 3:
        sign = input("Введите знак с сравнения. Вот список знаков: >, <, >=, <=, ==, !=\n")
        quantity = int(input("Введите количество с которым хотите сравнивать\n"))
        print("Вывод по условию(стоимость", sign, " ", quantity, ": ")
        sort_cost(mylist, sign, quantity)
    elif key == 4:
        printlist(mylist)

    print("Введите:\n1 - Если хотите сохранить в файл\n0 - Если не хотите сохранять в файл")
    check = int(input())
    if check == 1:
        fields = ["п»їNumber", "Name", "Text", "Likes"]
        with open('output.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for row in mylist:
                writer.writerow(row)
        print("Сохранение завершено")
    else:
        exit()
