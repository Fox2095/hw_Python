# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])


    def valid(day, month, year):
        if 1 <= day <= 31 and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
            print('Всё в порядке! В данном месяце 31 день!')
        elif 1 <= day <= 30 and (month == 4 or month == 6 or month == 9 or month == 11):
            print('Всё в порядке! В этом месяце 30 дней!')
        elif 1 <= day <= 29 and month == 2 and (year % 4 == 0 or year % 400 == 0):
            print('Всё в порядке! Этот год является високосный!')
        elif month == 2 and 1 <= day <= 28 and (year % 4 != 0 or year % 400 != 0):
           print('Всё в порядке! В этом месяце 28 дней!')
        else:
            print('Вы ввели не корректные данные!!!')

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


today = Date('25 - 03 - 2021')
print(today)
print(Date.extract('20 - 1 - 1995'))
print(Date.valid(20, 1, 1995))
print(Date.extract('33 - 12 - 2020'))
print(Date.valid(33, 12, 2020))
print(Date.extract('29 - 02 - 2020'))
print(Date.valid(29, 2, 2020))
print(Date.extract('29 - 02 - 2021'))
print(Date.valid(29, 2, 2021))
print(Date.extract('29 - 11 - 2020'))
print(Date.valid(29, 11, 2020))
print(Date.extract('31 - 4 - 2020'))
print(Date.valid(31, 4, 2020))
print(Date.extract('11 - 02 - 2021'))
print(Date.valid(11, 2, 2021))

