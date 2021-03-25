# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу
# на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.

class Division:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def division_of_numbers (numerator, denominator):
        try:
            return (numerator / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = Division(10, 100)
print(Division.division_of_numbers(10, 0))
print(Division.division_of_numbers(10, 0.1))
print(div.division_of_numbers(100, 0))