# После выполнения домашнего задания по определению есть ли номерные знаки в списке,
#
# переделать программу, таким образом,
#
# 1 . чтоб функция получала на вход введенные данные с командной строки и
#
#
#
# Проверяла на соответствие Длине введенного текста
# Возвращала 6 значений полученных из введенного номера (по 2 буквы и 4 цифры)
# Если общее количество символов больше или меньше 8 (во введенных данных) возвращала False
# 2. Написать вторую функцию, которая будет считать сумму чисел внутри последовательности.
#
# Функция должна вернуть сумму
#
# 3.Использовать эти функции в изначальной задаче

import json


def uniq(a): # функция для определения уникальных, не повторяющихся номерных знаков
    set_plates_list = set(a) # переводим список в сет, в сете не бывает повторяющихся элементов
    len_set = len(set_plates_list) # находим длину сета
    print("Number of unique license plates: ", len_set)


def sum_num(b):  # функция для определения суммы чисел в введенном знаке
    sum_digit = 0
    for i in b:
        if i.isdigit():
            sum_digit += int(i)
    print("The sum of the numbers in the entered license plate:", sum_digit)


def num_let(c):
    tpl = [c[:2], int(c[2]), int(c[3]), int(c[4]), int(c[5]), c[6:]]
    print("Letters and numbers in plate: ", tpl)


def presence(d): # функция для проверки наличия введенного знака в списке
    some_plate = input("Enter plate: ")
    while len(some_plate) != 8 or not some_plate[:2].isalpha() or not some_plate[6:].isalpha() or not some_plate[
                                                                                                      2:6].isdigit():
        print("Not a plate")
        some_plate = input("Enter plate: ")
    else:
        a = some_plate.upper() # делаем все символы в верхнем регистре, как в списке
        while a not in plates_list:
            print("Entered plate is not in the list!")
            some_plate = input("Enter plate: ")
            a = some_plate.upper()
        else:
            print("Entered plate is in the list!")
            sum_num(a)
            num_let(a)


with open("text.json", 'r') as file: # открывaем файл для чтения
    text = file.read() # читаем файл
    plates_list = json.loads(text) # открываем как json, это позволяет прочитать содержимое файла в виде списка

uniq(plates_list)
presence(plates_list)







