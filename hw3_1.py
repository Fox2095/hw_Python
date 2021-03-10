# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(*args):

    try:
        number1 = int(input("Введите первое число "))
        number2 = float(input("Введите второе число "))
        result = number1 / number2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "Вы не можете использовать ноль в качестве разделителя "

    return result

    '''
 if number2 != 0:
 return number1 / number2
 else:
 print("Вы не можете использовать ноль в качестве разделителя ")
    '''


print(f'Результат {division()}')