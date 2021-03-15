# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open('testfile5_1.txt', 'w')
type_text = input('Введите текст \n')
while type_text:
    f.writelines(type_text)
    type_text = input('Введите текст \n')
    if not type_text:
        break

f.close()
f = open('testfile5_1.txt', 'r')
content = f.readlines()
print(content)
f.close()

