# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Оклад': wage, 'Премия': bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['Оклад'] + self._income['Премия']

n=input('Введите своё имя: ')
s=input('Введите фамилию: ')
p=input('Введите свою должность: ')
w=float(input('Введите оклад: '))
b=float(input('Введите премию: '))
date=Position(n,s,p,w,b)
print(f'Ваши данные: {date.name}, {date.surname}, {date.position}, {date._income}')
print(f'{date.get_full_name()} ваша зароботная плата состовляет {date.get_full_salary()}')