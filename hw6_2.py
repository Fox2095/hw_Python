# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, _length, _width, weight, thickness):
        self._length = _length
        self._width =_width
        self.weight = weight
        self.thickness = thickness

    def road_f(self):
        l=self._length
        w=self._width
        we=self.weight
        t=self.thickness
        troad =l*w*we*t/1000
        return print(f'Масса асфальта: {l} м * {w} м * {we} кг * {t} см = ", {troad}, "т')

r = Road(20, 5000, 25, 5)
r.road_f()
r = Road((float(input('Введите длину (м) : '))),(float(input('Введите ширину (м) : '))), (float(input('Введите массу (кг) : '))), (float(input('Введите толщину (см): '))))
r.road_f()