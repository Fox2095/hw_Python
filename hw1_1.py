# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните
# в переменные, выведите на экран.

name = "Татьяна"
surname = "Копасова"
cat = 2
dollar_rate = 74.63

print('Добрый день! Меня зовут', name, surname)
print('У меня', cat,'кошки')
print('Курс доллара', dollar_rate)

name1 = input('Введите ваше имя - ')
print('Добро пожаловать ', name1)
animals = int(input('Сколько у вас животных? '))
dollar_rate1 = float(input('Введите курс доллара на текущий момент - '))
print('Вы ввели колличество животных - ', animals, ' И Теккущий курс доллара - ', dollar_rate1)

# Типы переменных
print(type(name)) #<class 'str'>
print(type(surname)) #<класс 'str'>
print(type(cat)) #<класс 'int'>
print(type(dollar_rate)) #<класс 'float'>
print(type(name1)) #<class 'str'>
print(type(animals)) #<класс 'int'>
print(type(dollar_rate1)) #<класс 'float'>