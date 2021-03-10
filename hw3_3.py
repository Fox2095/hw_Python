# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(number1 , number2, number3):
    if number1 >= number3 and number2 >= number3:
        return number1 + number2
    elif number1 > number2 and number1 < number3:
        return number1 + number3
    else:
        return number2 + number3

num_ber1 = int(input("Введите первое число: "))
num_ber2 = int(input("Введите второе число: "))
num_ber3 = int(input("Введите третье число: "))

result = my_func(num_ber1,num_ber2,num_ber3)

print(f'Результат - {result}')