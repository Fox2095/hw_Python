# 2. Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(*args, **kwargs):
    return args, kwargs

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = int(input('Введите год рождения: '))
city = input('Введите город проживания: ')
email = input('Введите email: ')
telephone = int(input('Введите номер телефона: '))

my_func(name='Tatyana', surname='Kopasova',year=1995,city='Moscow',email='ms.tkopasova@yandex.ru',telephone=+79100009591)
print(f' Результат: { my_func(name,surname,year,city,email,telephone)} ')