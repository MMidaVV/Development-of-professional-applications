import os
import csv


class Table:
    def __init__(self):
        self.mylist = {}
        self.name_file = None
        self.i = 0
        self.n = 0

    def set_attribute(self, name_file):
        self.__setattr__("name_file", name_file)

    def read(self):
        with open(name_file, newline='') as file:
            reader = csv.DictReader(file, delimiter=";")
            self.mylist = [row for row in reader]

    @staticmethod
    def directory():
        print("Количество файлов в директории:", len(os.listdir(path=".")))

    def __iter__(self):
        return self

    def __next__(self):
        self.n = len(self.mylist)
        if self.i < self.n:
            i = self.mylist[self.i]
            self.i += 1
            return i
        else:
            raise StopIteration

    def __repr__(self):
        return "Name table: \n" + name_file + "\nKeys:\n" + ", ".join(i for i in self.mylist[0])


class Posts(Table):
    def __init__(self):
        super().__init__()
        self.new_list = None
        Table.read(self)

    def sort_cost(self):
        sign = input("Введите знак с сравнения. Вот список знаков: >, <, >=, <=, ==, !=\n")
        quantity = int(input("Введите количество с которым хотите сравнивать\n"))
        print("Вывод по условию(стоимость", sign, " ", quantity, ": ")
        for x in self.mylist:
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

    def sort_name(self):
        print("Сортировка по названию(по убыванию):")
        self.mylist = sorted(self.mylist, key=lambda x: x['Name'])
        Posts.printlist(self.mylist)

    def sort_like(self):
        print("Сортировка по стоимости(по убыванию):")
        self.mylist = sorted(self.mylist, key=lambda x: x['Likes'])
        self.mylist = list(reversed(self.mylist))
        Posts.printlist(self.mylist)

    def printlist(self):
        for x in self:
            print(x)

    def save_file(self, check):
        if check == 1:
            fields = ["п»їNumber", "Name", "Text", "Likes"]
            with open('output.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                for row in self.mylist:
                    writer.writerow(row)
            print("Сохранение завершено")


Table.directory()
name_file = input("Введите название файла(пример: text.txt)\n")
post = Posts()
post.set_attribute(name_file)
print(post)
key = int(
        input("Введите \n1 - если хотите увидеть сортировку файла по именам в алфавитном порядке, \n2 - если хотите "
              "увидеть сортировку по лайкам по возрастанию, \n3 - если хотите увидеть только строки с определённым "
              "количеством лайков, \n4 - если просто хотите вывести все строки\n")
)
if key == 1:
    post.sort_name()
elif key == 2:
    post.sort_like()
elif key == 3:
    post.sort_cost()
elif key == 4:
    post.printlist()
check = int(input("Введите:\n1 - Если хотите сохранить в файл\n0 - Если не хотите сохранять в файл\n"))
post.save_file(check)



