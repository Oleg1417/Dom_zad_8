# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных
"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""
phone_book = 'Phon_number.txt'

def Fill_data():
    print('Введите данные в формате: Фамилия Имя телефон: ')
    with open(phone_book, 'a') as save:
        save.writelines(input() + '\n')


def Names():
    print('Введите параметр поиска: ')
    par = str(input())
    return par


def Find_people(par):
    with open(phone_book, 'r', encoding='utf-8') as save:
        for line in save:
            if str(par).lower() in str(line).lower():
                print(line)
        return line


def Change_data(par):
    text = ""
    with open(phone_book, 'r', encoding='utf-8') as save:
        for line in save:
            if str(par).lower() in str(line).lower():
                print("Вы хотите заменить этот контакт:\n "+line)
                c = int(input("1 - да\n2 - нет\n"))
                if c == 1:
                  text = text+input("введите новые данные:\n")+"\n"
                else: text = text+line
            else:
                text = text+line
    with open(phone_book, 'w') as save:
        save.writelines(text)


def Delete_Name(par):
    text = ""
    with open(phone_book, 'r', encoding='utf-8') as save:
        for line in save:
            if str(par).lower() in str(line).lower():
                print("Вы хотите удалить этот контакт:\n "+line)
                c = int(input("1 - да\n2 - нет\n"))
                if c == 1:
                    text = text
                else:
                    text = text+line
            else:
                text = text+line
    with open(phone_book, 'w') as save:
        save.writelines(text)


n = int(input("Введите:\n1 - для поиска в телефонной книге\n2 - для добовления контактоа\n3 - для изменения данных\n4 - для удаления контакта\n"))
if n == 1:
    Find_people(Names())
elif n == 2:
    Fill_data()
elif n == 3:
    Change_data(Names())
elif n == 4:
    Delete_Name(Names())
else:
    print("comand not found")
