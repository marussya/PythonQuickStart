# coding: utf-8

import os
import psutil

print("Добро пожаловать на курс Python Quick Start!")

name = input("Введите имя: ")

print(name, ", здравствуйте!")

answer = input("Вы хотите поработать? (Y/N) ")

# PEP-8
if answer == 'y':
    print("Отлично!")
    print("Я умею: ")
    print(" [1] - выведу список файлов")
    print(" [2] - выведу информацию о системе")
    print(" [3] - выведу список процессов")
    do = int(input("Укажите номер действия: "))

    if do == 1:
        print(os.listdir())
    elif do == 2:
        pass
    elif do == 3:
        print(psutil.pids())
    else:
        pass

elif answer == "n":
    print("До свидания!")
else:
    print("Неизвестный ответ.")
