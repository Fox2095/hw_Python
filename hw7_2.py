# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Сlothes(ABC):
    def __init__(self, parametr):
        self.parametr = parametr

    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {self.parametr / 6.5 + 0.5 + 2 * self.parametr + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Что-то различное абстрактное'

class Coat(Сlothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.parametr / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Что-то изменить абстрактную секунду'

class Costume(Сlothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.parametr + 0.3 :.2f} ткани'

    def abstract(self):
        pass

coat = Coat(987)
costume = Costume(80)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())
