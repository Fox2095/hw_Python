# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

data = input("Введите данные: ")
list_data = data.split(' ')
for i, elem in enumerate(list_data, 1):
    if len(elem) > 10:
        elem = elem[0:10]
    print(f"{i}. - {elem}")